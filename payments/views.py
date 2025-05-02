from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
import uuid
from .models import Payment, Fee
from students.models import Student

@login_required
def payment_list(request):
    payments = Payment.objects.all().select_related('student', 'fee')
    return render(request, 'payments/payment_list.html', {'payments': payments})

@login_required
def payment_detail(request, receipt_number):
    payment = get_object_or_404(Payment, receipt_number=receipt_number)
    return render(request, 'payments/payment_detail.html', {'payment': payment})

@login_required
def make_payment(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    pending_fees = Fee.objects.filter(payment__student=student, payment__status='PENDING')
    
    if request.method == 'POST':
        fee = get_object_or_404(Fee, id=request.POST.get('fee'))
        amount_paid = float(request.POST.get('amount_paid'))
        
        if amount_paid <= 0 or amount_paid > fee.amount:
            messages.error(request, 'Invalid payment amount')
            return redirect('payments:make_payment', student_id=student_id)
        
        payment = Payment.objects.create(
            student=student,
            fee=fee,
            amount_paid=amount_paid,
            payment_method=request.POST.get('payment_method'),
            status='PAID',
            transaction_id=str(uuid.uuid4()),
            receipt_number=f'REC-{timezone.now().strftime("%Y%m%d")}-{uuid.uuid4().hex[:6].upper()}',
            notes=request.POST.get('notes', '')
        )
        
        messages.success(request, 'Payment processed successfully')
        return redirect('payments:payment_detail', receipt_number=payment.receipt_number)
    
    context = {
        'student': student,
        'pending_fees': pending_fees,
        'payment_methods': Payment.PAYMENT_METHODS
    }
    return render(request, 'payments/make_payment.html', context)
