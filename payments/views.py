from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.db.models import Sum, Count
from django.core.paginator import Paginator
import uuid
from .models import Payment, Fee
from students.models import Student

@login_required
def payment_list(request):
    # Get filter parameters
    status = request.GET.get('status')
    student_id = request.GET.get('student_id')
    fee_type = request.GET.get('fee_type')

    # Base queryset
    payments = Payment.objects.select_related('student', 'fee').all()

    # Apply filters
    if status:
        payments = payments.filter(status=status)
    if student_id:
        payments = payments.filter(student__student_id__icontains=student_id)
    if fee_type:
        payments = payments.filter(fee__id=fee_type)    # Calculate statistics for different payment statuses
    paid = Payment.objects.filter(status='PAID').aggregate(
        amount=Sum('amount_paid'),
        count=Count('id')
    )
    pending = Payment.objects.filter(status='PENDING').aggregate(
        amount=Sum('amount_paid'),
        count=Count('id')
    )
    overdue = Payment.objects.filter(status='OVERDUE').aggregate(
        amount=Sum('amount_paid'),
        count=Count('id')
    )
    total = Payment.objects.aggregate(
        amount=Sum('amount_paid'),
        count=Count('id')
    )

    # Pagination
    paginator = Paginator(payments, 10)  # Show 10 payments per page
    page = request.GET.get('page')
    payments = paginator.get_page(page)    
    context = {
        'payments': payments,
        'payment_status_choices': Payment.PAYMENT_STATUS,
        'fee_types': Fee.objects.all(),
        'selected_status': status,
        'student_id': student_id,
        'selected_fee': fee_type,
        'total_amount': total['amount'] or 0,
        'total_count': total['count'] or 0,
        'total_paid_amount': paid['amount'] or 0,
        'paid_count': paid['count'] or 0,
        'total_pending_amount': pending['amount'] or 0,
        'pending_count': pending['count'] or 0,
        'total_overdue_amount': overdue['amount'] or 0,
        'overdue_count': overdue['count'] or 0,
    }

    return render(request, 'payments/payment_list.html', context)

@login_required
def payment_detail(request, receipt_number):
    payment = get_object_or_404(Payment, receipt_number=receipt_number)
    return render(request, 'payments/payment_detail.html', {'payment': payment})

@login_required
def make_payment(request, student_id=None):
    # If student_id is provided, get that specific student
    student = None
    if student_id:
        student = get_object_or_404(Student, student_id=student_id)
    
    # Get all active fees
    fees = Fee.objects.filter(due_date__gte=timezone.now())
    
    # Get all students for the dropdown if no specific student is selected
    students = Student.objects.all() if not student else None
    
    if request.method == 'POST':
        selected_student_id = student_id or request.POST.get('student')
        selected_fee_id = request.POST.get('fee')
        amount_paid = request.POST.get('amount_paid')
        payment_method = request.POST.get('payment_method')
        
        if not all([selected_student_id, selected_fee_id, amount_paid, payment_method]):
            messages.error(request, 'Vui lòng điền đầy đủ thông tin thanh toán.')
            return render(request, 'payments/make_payment.html', {
                'student': student,
                'students': students,
                'fees': fees
            })
        
        # Get the selected student and fee
        student = get_object_or_404(Student, student_id=selected_student_id)
        fee = get_object_or_404(Fee, id=selected_fee_id)
        
        # Create unique transaction ID and receipt number
        transaction_id = str(uuid.uuid4())
        receipt_number = f"PMT-{timezone.now().strftime('%Y%m%d')}-{str(uuid.uuid4())[:8]}"
        
        # Create the payment
        payment = Payment.objects.create(
            student=student,
            fee=fee,
            amount_paid=amount_paid,
            payment_method=payment_method,
            status='PAID',
            transaction_id=transaction_id,
            receipt_number=receipt_number
        )
        
        messages.success(request, f'Thanh toán thành công. Mã biên nhận: {receipt_number}')
        return redirect('payments:payment_detail', receipt_number=receipt_number)
    
    return render(request, 'payments/make_payment.html', {
        'student': student,
        'students': students,
        'fees': fees
    })

@login_required
def process_payment(request, payment_id):
    payment = get_object_or_404(Payment, id=payment_id)
    
    if payment.status != 'PENDING':
        messages.error(request, 'Chỉ có thể xử lý các khoản thanh toán đang chờ')
        return redirect('payments:payment_list')
    
    payment.status = 'PAID'
    payment.payment_date = timezone.now()
    payment.save()
    
    messages.success(request, f'Đã xác nhận thanh toán thành công cho {payment.student.full_name}')
    return redirect('payments:payment_list')
