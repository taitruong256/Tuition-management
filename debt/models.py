from django.db import models
from accounts.models import StudentUser
from curriculum.models import Semester

class TuitionDebt(models.Model):
    STATUS_CHOICES = [
        ('unpaid', 'Chưa thanh toán'),
        ('paid', 'Đã thanh toán'),
    ]
    student = models.ForeignKey(StudentUser, on_delete=models.CASCADE, related_name='tuition_debts')
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='tuition_debts')
    theory_credits = models.PositiveIntegerField(default=0, verbose_name='Số TC lý thuyết')
    practice_credits = models.PositiveIntegerField(default=0, verbose_name='Số TC thực hành')
    total_amount = models.PositiveBigIntegerField(default=0, verbose_name='Tổng tiền')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='unpaid')

    def calculate_amount(self):
        return self.theory_credits * 700_000 + self.practice_credits * 1_000_000

    def save(self, *args, **kwargs):
        self.total_amount = self.calculate_amount()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student} - {self.semester} ({self.get_status_display()})"

class OtherFee(models.Model):
    STATUS_CHOICES = [
        ('unpaid', 'Chưa thanh toán'),
        ('paid', 'Đã thanh toán'),
    ]
    student = models.ForeignKey(StudentUser, on_delete=models.CASCADE, related_name='other_fees')
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='other_fees')
    name = models.CharField(max_length=255, verbose_name='Tên khoản thu')
    amount = models.PositiveBigIntegerField(verbose_name='Số tiền')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='unpaid')

    def __str__(self):
        return f"{self.student} - {self.name} ({self.get_status_display()})"