from django.contrib import admin
from .models import Invoice

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'payment', 'created_at', 'pdf_file')
    search_fields = ('student__full_name', 'payment__description')
    list_filter = ('created_at',)
