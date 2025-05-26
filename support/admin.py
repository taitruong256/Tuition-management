from django.contrib import admin
from .models import SupportRequest

@admin.register(SupportRequest)
class SupportRequestAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'status', 'created_at', 'replied_at')
    list_filter = ('status', 'created_at')
    search_fields = ('student__full_name', 'subject', 'content')
