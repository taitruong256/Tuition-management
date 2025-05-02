from django.db import models
from students.models import Student
from django.utils import timezone

class Fee(models.Model):
    name = models.CharField(max_length=100)  # e.g., "Tuition Fee", "Library Fee"
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    academic_year = models.CharField(max_length=9)  # e.g., "2024-2025"
    semester = models.CharField(max_length=20)  # e.g., "Fall", "Spring"
    due_date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.academic_year} ({self.semester})"

class Payment(models.Model):
    PAYMENT_STATUS = [
        ('PENDING', 'Pending'),
        ('PAID', 'Paid'),
        ('OVERDUE', 'Overdue'),
        ('CANCELLED', 'Cancelled')
    ]

    PAYMENT_METHODS = [
        ('CASH', 'Cash'),
        ('BANK_TRANSFER', 'Bank Transfer'),
        ('CREDIT_CARD', 'Credit Card'),
        ('OTHER', 'Other')
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    fee = models.ForeignKey(Fee, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(default=timezone.now)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    status = models.CharField(max_length=20, choices=PAYMENT_STATUS)
    transaction_id = models.CharField(max_length=100, unique=True)
    receipt_number = models.CharField(max_length=50, unique=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Payment {self.receipt_number} - {self.student.student_id}"

    class Meta:
        ordering = ['-payment_date']
