from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Student
from payments.models import Payment, Fee

@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

@login_required
def student_detail(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    payments = Payment.objects.filter(student=student)
    pending_fees = Fee.objects.filter(payment__student=student, payment__status='PENDING')
    return render(request, 'students/student_detail.html', {
        'student': student,
        'payments': payments,
        'pending_fees': pending_fees
    })
