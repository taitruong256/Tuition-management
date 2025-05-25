from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Curriculum

# Create your views here.

# Danh sách tất cả chương trình khung

def curriculum_list(request):
    curriculums = Curriculum.objects.all()
    return render(request, 'curriculum/curriculum_list.html', {'curriculums': curriculums})

# Chi tiết một chương trình khung

def curriculum_detail(request, pk):
    curriculum = get_object_or_404(Curriculum, pk=pk)
    return render(request, 'curriculum/curriculum_detail.html', {'curriculum': curriculum})

@login_required
def my_curriculum(request):
    try:
        curriculum = request.user.curriculum
    except AttributeError:
        curriculum = None
    return render(request, 'curriculum/my_curriculum.html', {'curriculum': curriculum})
