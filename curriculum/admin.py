from django.contrib import admin
from .models import CurriculumFramework, Semester, SubjectGroup, Subject

# Register your models here.
admin.site.register(CurriculumFramework)
admin.site.register(Semester)
admin.site.register(SubjectGroup)
admin.site.register(Subject)
