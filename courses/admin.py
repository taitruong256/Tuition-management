from django.contrib import admin
from .models import Course, CourseRegistration

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'class_code', 'name', 'credits', 'is_mandatory', 'term')
    search_fields = ('course_id', 'class_code', 'name')
    list_filter = ('is_mandatory', 'term')

@admin.register(CourseRegistration)
class CourseRegistrationAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'registration_type', 'term', 'registration_date')
    list_filter = ('registration_type', 'term')
    search_fields = ('student__student_id', 'student__full_name', 'course__course_id', 'course__name')
