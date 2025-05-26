from django.db import models
from accounts.models import StudentUser
from curriculum.models import Semester

class OnlinePayment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Chờ xử lý'),
        ('success', 'Thành công'),
        ('failed', 'Thất bại'),
    ]
    student = models.ForeignKey(StudentUser, on_delete=models.CASCADE, related_name='online_payments')
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='online_payments')
    amount = models.PositiveBigIntegerField(verbose_name='Số tiền')
    payment_method = models.CharField(max_length=50, verbose_name='Phương thức', default='Chuyển khoản')
    transaction_id = models.CharField(max_length=100, blank=True, null=True, verbose_name='Mã giao dịch')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    confirmed_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.student} - {self.amount} ({self.get_status_display()})"
