from django.contrib import admin
from .models import OnlinePayment

@admin.register(OnlinePayment)
class OnlinePaymentAdmin(admin.ModelAdmin):
    list_display = ('student', 'semester', 'amount', 'payment_method', 'transaction_id', 'status', 'created_at', 'confirmed_at')
    list_filter = ('status', 'payment_method', 'semester')
    search_fields = ('student__full_name', 'transaction_id')
