from django.contrib import admin
from .models import Room, Lecturer, ClassSubject, Registration

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')

@admin.register(ClassSubject)
class ClassSubjectAdmin(admin.ModelAdmin):
    list_display = ('subject', 'type', 'room', 'lecturer1', 'lecturer2', 'schedule', 'max_students')
    list_filter = ('type', 'room', 'subject')
    search_fields = ('subject__name',)

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('student', 'class_subject', 'registered_at')
    list_filter = ('class_subject', 'student')
    search_fields = ('student__full_name', 'class_subject__subject__name')
