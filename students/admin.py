from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'full_name', 'class_name', 'major', 'academic_year', 'education_level')
    search_fields = ('student_id', 'full_name', 'class_name', 'major')
    list_filter = ('education_level', 'education_type', 'gender', 'academic_year')
    fieldsets = (
        ('Thông tin cơ bản', {
            'fields': ('student_id', 'full_name', 'class_name', 'gender', 'date_of_birth', 'place_of_birth')
        }),
        ('Thông tin đào tạo', {
            'fields': ('major', 'academic_year', 'education_level', 'education_type')
        }),
    )
