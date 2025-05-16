from django.shortcuts import render, get_object_or_404, redirect
from .models import CurriculumFramework
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseForbidden
from django.contrib import messages

# Create your views here.

# View chỉ xem, ai cũng xem được

def curriculum_framework_list(request):
    frameworks = CurriculumFramework.objects.all()
    return render(request, 'curriculum/curriculum_framework_list.html', {'frameworks': frameworks})

# Ví dụ view thêm (chỉ admin mới được phép)
@login_required
@user_passes_test(lambda u: u.is_superuser)
def curriculum_framework_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        total_credits = request.POST.get('total_credits')
        is_active = request.POST.get('is_active') == 'on'
        
        CurriculumFramework.objects.create(
            name=name,
            description=description,
            total_credits=total_credits,
            is_active=is_active
        )
        messages.success(request, 'Thêm chương trình khung thành công!')
        return redirect('curriculum:curriculum_framework_list')
    
    return render(request, 'curriculum/curriculum_framework_form.html')

@login_required
@user_passes_test(lambda u: u.is_superuser)
def curriculum_framework_update(request, pk):
    framework = get_object_or_404(CurriculumFramework, pk=pk)
    
    if request.method == 'POST':
        framework.name = request.POST.get('name')
        framework.description = request.POST.get('description')
        framework.total_credits = request.POST.get('total_credits')
        framework.is_active = request.POST.get('is_active') == 'on'
        framework.save()
        
        messages.success(request, 'Cập nhật chương trình khung thành công!')
        return redirect('curriculum:curriculum_framework_list')
    
    return render(request, 'curriculum/curriculum_framework_form.html', {'framework': framework})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def curriculum_framework_delete(request, pk):
    framework = get_object_or_404(CurriculumFramework, pk=pk)
    
    if request.method == 'POST':
        framework.delete()
        messages.success(request, 'Xóa chương trình khung thành công!')
        return redirect('curriculum:curriculum_framework_list')
    
    return render(request, 'curriculum/curriculum_framework_confirm_delete.html', {'framework': framework})
