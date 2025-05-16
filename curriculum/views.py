from django.shortcuts import render
from .models import CurriculumFramework

# Create your views here.

def curriculum_framework_list(request):
    frameworks = CurriculumFramework.objects.all()
    return render(request, 'curriculum/curriculum_framework_list.html', {'frameworks': frameworks})
