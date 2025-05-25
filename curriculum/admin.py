from django.contrib import admin
from .models import Curriculum, Semester, Subject

class SubjectInline(admin.TabularInline):
    model = Subject
    extra = 1

class SemesterInline(admin.StackedInline):
    model = Semester
    extra = 1
    show_change_link = True

class SemesterAdmin(admin.ModelAdmin):
    inlines = [SubjectInline]
    list_display = ('name', 'curriculum', 'order')
    list_filter = ('curriculum',)

class CurriculumAdmin(admin.ModelAdmin):
    inlines = [SemesterInline]
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Curriculum, CurriculumAdmin)
admin.site.register(Semester, SemesterAdmin)
admin.site.register(Subject)
