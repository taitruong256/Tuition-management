from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import StudentUser

@admin.register(StudentUser)
class StudentUserAdmin(UserAdmin):
    model = StudentUser
    list_display = ('student_id', 'full_name', 'email', 'gender', 'status', 'class_name', 'major', 'faculty')
    fieldsets = (
        (None, {'fields': ('student_id', 'email', 'password')}),
        ('Thông tin cá nhân', {'fields': ('full_name', 'gender', 'status', 'class_name', 'major', 'faculty', 'specialization', 'course_year', 'education_level', 'education_type', 'campus')}),
        ('Quyền', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Thông tin khác', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('student_id', 'email', 'full_name', 'password1', 'password2', 'gender', 'status', 'class_name', 'major', 'faculty', 'specialization', 'course_year', 'education_level', 'education_type', 'campus', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )
    readonly_fields = ('last_login', 'date_joined')
    search_fields = ('student_id', 'full_name', 'email')
    ordering = ('student_id',)
