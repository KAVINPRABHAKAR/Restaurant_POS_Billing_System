import pandas as pd
import numpy as np
from django.db.models import Sum, Count
from django.utils import timezone
from datetime import timedelta
from .models import Order, OrderItem, MenuItem

def get_sales_analytics():
    # 1. Fetch data from Database
    orders_queryset = Order.objects.all().values('order_date', 'total_amount')
    order_items_queryset = OrderItem.objects.all().values('item__name', 'quantity')

    # Handle empty database case
    if not orders_queryset.exists():
        return {
            'total_revenue': 0,
            'total_orders': 0,
            'avg_order': 0,
            'most_sold_labels': [],
            'most_sold_values': [],
            'trend_labels': [],
            'trend_values': [],
            'top_items': []
        }

    # 2. Convert to Pandas DataFrames for advanced processing
    df_orders = pd.DataFrame(list(orders_queryset))
    df_items = pd.DataFrame(list(order_items_queryset))

    # 3. Revenue Analytics using NumPy & Pandas
    total_revenue = np.sum(df_orders['total_amount'])
    avg_order_value = np.mean(df_orders['total_amount'])
    total_orders = len(df_orders)

    # 4. Most Sold Items (Top 5)
    most_sold = df_items.groupby('item__name')['quantity'].sum().sort_values(ascending=False).head(5)
    
    # 5. Daily Sales Trend (Last 7 Days)
    df_orders['order_date'] = pd.to_datetime(df_orders['order_date'])
    daily_trend = df_orders.groupby(df_orders['order_date'].dt.date)['total_amount'].sum().tail(7)

    # 6. Django-specific list for templates
    # This ensures your existing table loops still work
    top_items_list = [
        {'item__name': name, 'total_qty': qty} 
        for name, qty in most_sold.items()
    ]

    return {
        'total_revenue': round(float(total_revenue), 2),
        'total_orders': total_orders,
        'avg_order': round(float(avg_order_value), 2),
        'most_sold_labels': list(most_sold.index),
        'most_sold_values': [int(x) for x in most_sold.values],
        'trend_labels': [str(date) for date in daily_trend.index],
        'trend_values': [float(x) for x in daily_trend.values],
        'top_items': top_items_list,
    }