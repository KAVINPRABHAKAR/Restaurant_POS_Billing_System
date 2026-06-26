from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
from .models import Category, MenuItem, Order, OrderItem

# --- ADMIN INTERFACE BRANDING ---
admin.site.site_header = "POS PRO MANAGEMENT PORTAL"
admin.site.site_title = "POS PRO Admin"
admin.site.index_title = "Restaurant Operations & User Control"

# --- USER ROLE MANAGEMENT ---
admin.site.unregister(User)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """
    Customizes the User list to show if they are a Manager or Cashier.
    """
    list_display = ('username', 'email', 'get_role', 'is_active', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'groups')

    def get_role(self, obj):
        if obj.is_superuser:
            return "System Admin"
        elif obj.groups.filter(name='Manager').exists() or obj.is_staff:
            return "Manager"
        return "Cashier"
    get_role.short_description = 'Designated Role'

    def save_model(self, request, obj, form, change):
        """
        Auto-assign groups based on staff status.
        If 'Staff status' is checked, they become a Manager.
        """
        super().save_model(request, obj, form, change)
        
        manager_group, _ = Group.objects.get_or_create(name='Manager')
        cashier_group, _ = Group.objects.get_or_create(name='Cashier')

        if obj.is_staff or obj.is_superuser:
            obj.groups.add(manager_group)
            obj.groups.remove(cashier_group)
        else:
            obj.groups.add(cashier_group)
            obj.groups.remove(manager_group)

# --- RESTAURANT INVENTORY MANAGEMENT ---

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'status_badge')
    list_filter = ('category',)
    search_fields = ('name',)
    list_editable = ('price', 'stock')

    def status_badge(self, obj):
        from django.utils.html import format_html
        if obj.stock <= 5:
            # FIXED: Added proper placeholder {} and arguments to fix TypeError
            return format_html('<span style="color: {}; font-weight: bold;">{}</span>', 'red', 'Low Stock')
        return format_html('<span style="color: {};">{}</span>', 'green', 'Available')
    status_badge.short_description = 'Inventory Status'

# --- ORDER & TRANSACTION MANAGEMENT ---

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('item', 'quantity', 'price_at_order')
    can_delete = False

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_date', 'cashier', 'total_amount')
    list_filter = ('order_date', 'cashier')
    search_fields = ('id', 'cashier__username')
    inlines = [OrderItemInline]
    
    # Ensure sales history cannot be altered manually
    readonly_fields = (
        'order_date', 'cashier', 'subtotal', 'gst_amount', 
        'service_charge', 'discount_amount', 'total_amount', 'coupon_code'
    )

    # Professional touch: Prevent manual addition of orders via admin to maintain integrity
    def has_add_permission(self, request):
        return False