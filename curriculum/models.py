from django.db import models
from django.core.exceptions import ValidationError

class Curriculum(models.Model):
    name = models.CharField(max_length=255, verbose_name='Tên chương trình khung')

    def __str__(self):
        return self.name

class Semester(models.Model):
    curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE, related_name='semesters')
    name = models.CharField(max_length=100, verbose_name='Tên học kỳ')
    order = models.PositiveIntegerField(verbose_name='Thứ tự học kỳ')

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.name} ({self.curriculum})"

class Subject(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='subjects')
    code = models.CharField(max_length=20, verbose_name='Mã môn học')
    name = models.CharField(max_length=255, verbose_name='Tên môn học')
    credits = models.PositiveIntegerField(verbose_name='Số tín chỉ')
    theory_credits = models.PositiveIntegerField(verbose_name='Số tín chỉ lý thuyết', default=0)
    practice_credits = models.PositiveIntegerField(verbose_name='Số tín chỉ thực hành', default=0)

    def clean(self):
        if self.theory_credits > self.credits:
            raise ValidationError('Số tín chỉ lý thuyết không được lớn hơn số tín chỉ môn học')
        self.practice_credits = self.credits - self.theory_credits

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.code} - {self.name} ({self.semester})"
