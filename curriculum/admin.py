from django.contrib import admin
from .models import Curriculum, Semester, Subject

class SubjectInline(admin.TabularInline):
    model = Subject
    extra = 1

class SemesterInline(admin.StackedInline):
    model = Semester
    extra = 1
    show_change_link = True

@admin.register(Curriculum)
class CurriculumAdmin(admin.ModelAdmin):
    inlines = [SemesterInline]
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    inlines = [SubjectInline]
    list_display = ('name', 'curriculum', 'order')
    list_filter = ('curriculum',)
    search_fields = ('name',)
    ordering = ('curriculum', 'order')

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'semester', 'credits', 'theory_credits', 'practice_credits')
    list_filter = ('semester',)
    search_fields = ('code', 'name')
    ordering = ('semester', 'code')

    def save_model(self, request, obj, form, change):
        try:
            obj.clean()
            super().save_model(request, obj, form, change)
        except Exception as e:
            self.message_user(request, str(e), level='error')
