from django.urls import path
from . import views

urlpatterns = [
    # --- Authentication ---
    path('', views.login_view, name='login'), 
    path('logout/', views.logout_view, name='logout'),

    # --- POS System ---
    path('pos/', views.pos_screen, name='pos_screen'),

    # --- Management & Analytics ---
    path('dashboard/', views.dashboard, name='dashboard'),
    path('inventory/', views.inventory_view, name='inventory'),
    path('sales-report/', views.sales_report, name='sales_report'),

    # --- Export Features ---
    # Changed name to 'export_pdf' to fix your NoReverseMatch error

    path('export-pdf/<int:order_id>/', views.export_pdf_bill, name='export_pdf'),
    
    # Global Excel Export
    path('export-excel/', views.export_excel_report, name='export_excel'),
]