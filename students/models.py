from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    program = models.CharField(max_length=100)  # e.g., "Computer Science", "Business"
    enrollment_date = models.DateField()
    
    def __str__(self):
        return f"{self.student_id} - {self.first_name} {self.last_name}"
    
    class Meta:
        ordering = ['student_id']
