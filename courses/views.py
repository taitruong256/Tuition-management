from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Course, CourseRegistration
from django.http import JsonResponse

@login_required
def course_registration(request):
    current_term = "HK3 (2024 - 2025)"  # You can make this dynamic
    available_courses = Course.objects.filter(term=current_term)
    
    try:
        student = request.user.student
        current_registrations = CourseRegistration.objects.filter(
            student=student,
            term=current_term
        ).select_related('course')
        total_registered_credits = sum(reg.course.credits for reg in current_registrations)
    except:
        student = None
        current_registrations = []
        total_registered_credits = 0
    
    context = {
        'current_term': current_term,
        'courses': available_courses,
        'student': student,
        'current_registrations': current_registrations,
        'total_registered_credits': total_registered_credits,
    }
    return render(request, 'courses/course_registration.html', context)

@login_required
def register_course(request):
    if request.method == 'POST':
        try:
            import json
            course_ids = json.loads(request.POST.get('courses', '[]'))
            registration_type = request.POST.get('registration_type', 'HỌC MỚI')
            
            # Kiểm tra tổng số tín chỉ
            total_credits = sum(Course.objects.filter(id__in=course_ids).values_list('credits', flat=True))
            if total_credits > 24:
                return JsonResponse({
                    'status': 'error',
                    'message': 'Tổng số tín chỉ không được vượt quá 24'
                })

            # Đăng ký các môn học
            registrations = []
            for course_id in course_ids:
                course = Course.objects.get(id=course_id)
                registration = CourseRegistration(
                    student=request.user.student,
                    course=course,
                    registration_type=registration_type,
                    term=course.term
                )
                registrations.append(registration)
            
            # Lưu tất cả đăng ký cùng một lúc
            CourseRegistration.objects.bulk_create(registrations)
            
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
