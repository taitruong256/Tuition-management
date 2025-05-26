from django.db import models
from accounts.models import StudentUser
from curriculum.models import Subject

class Room(models.Model):
    name = models.CharField(max_length=50, verbose_name='Tên phòng')
    description = models.TextField(blank=True, verbose_name='Mô tả')

    def __str__(self):
        return self.name

class Lecturer(models.Model):
    name = models.CharField(max_length=100, verbose_name='Tên giảng viên')
    email = models.EmailField(blank=True, verbose_name='Email')

    def __str__(self):
        return self.name

class ClassSubject(models.Model):
    TYPE_CHOICES = [
        ('LT', 'Lý thuyết'),
        ('TH', 'Thực hành'),
    ]
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='class_subjects', verbose_name='Môn học')
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Phòng học')
    theory_lecturer = models.ForeignKey(Lecturer, on_delete=models.SET_NULL, null=True, blank=True, related_name='theory_classes', verbose_name='Giảng viên lý thuyết')
    practice_lecturer = models.ForeignKey(Lecturer, on_delete=models.SET_NULL, null=True, blank=True, related_name='practice_classes', verbose_name='Giảng viên thực hành')
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, verbose_name='Loại lớp')
    practice_group = models.PositiveIntegerField(verbose_name='Nhóm thực hành', null=True, blank=True)
    schedule = models.CharField(max_length=100, blank=True, verbose_name='Thời gian học')
    max_students = models.PositiveIntegerField(default=50, verbose_name='Số lượng SV tối đa')

    def __str__(self):
        if self.type == 'TH':
            return f"{self.subject} - {self.get_type_display()} - Nhóm {self.practice_group}"
        return f"{self.subject} - {self.get_type_display()}"

    class Meta:
        unique_together = [('subject', 'type', 'practice_group')]

class Registration(models.Model):
    student = models.ForeignKey(StudentUser, on_delete=models.CASCADE, related_name='registrations')
    class_subject = models.ForeignKey(ClassSubject, on_delete=models.CASCADE, related_name='registrations')
    registered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'class_subject')

    def __str__(self):
        return f"{self.student} đăng ký {self.class_subject}"
