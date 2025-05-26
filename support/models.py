from django.db import models
from accounts.models import StudentUser

# Create your models here.

class SupportRequest(models.Model):
    # CATEGORY_CHOICES = [
    #     ('fee', 'Thắc mắc học phí'),
    #     ('payment', 'Sai sót thanh toán'),
    #     ('refund', 'Yêu cầu hoàn tiền'),
    #     ('other', 'Khác'),
    # ]
    student = models.ForeignKey(StudentUser, on_delete=models.CASCADE, related_name='support_requests')
    # category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    subject = models.CharField(max_length=255, verbose_name='Tiêu đề')
    content = models.TextField(verbose_name='Nội dung')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('pending','Chờ xử lý'),('resolved','Đã xử lý')], default='pending')
    admin_reply = models.TextField(blank=True, verbose_name='Phản hồi từ admin')
    replied_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.student} - {self.subject}"
