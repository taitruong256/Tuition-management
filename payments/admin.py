from django.contrib import admin
from .models import Payment, Fee

@admin.register(Fee)
class FeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'academic_year', 'semester', 'due_date')
    search_fields = ('name', 'academic_year')
    list_filter = ('academic_year', 'semester')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('student', 'fee', 'amount_paid', 'payment_date', 'status', 'payment_method')
    search_fields = ('student__student_id', 'student__first_name', 'transaction_id', 'receipt_number')
    list_filter = ('status', 'payment_method', 'payment_date')
    date_hierarchy = 'payment_date'
