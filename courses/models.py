from django.db import models
from students.models import Student

class Course(models.Model):
    course_id = models.CharField(max_length=20, unique=True, verbose_name='Mã MH')
    class_code = models.CharField(max_length=20, verbose_name='Mã HP')
    name = models.CharField(max_length=200, verbose_name='Tên môn học')
    credits = models.IntegerField(verbose_name='TC')
    is_mandatory = models.BooleanField(default=True, verbose_name='Bắt buộc')
    prerequisites = models.TextField(blank=True, null=True, verbose_name='Học phần tiên quyết')
    term = models.CharField(max_length=20, verbose_name='Học kỳ')
    enrolled_students = models.ManyToManyField(Student, through='CourseRegistration')

    def __str__(self):
        return f"{self.course_id} - {self.name}"

    class Meta:
        ordering = ['course_id']

class CourseRegistration(models.Model):
    REGISTRATION_TYPES = [
        ('HỌC MỚI', 'Học mới'),
        ('HỌC LẠI', 'Học lại'),
        ('HỌC CẢI THIỆN', 'Học cải thiện')
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    registration_type = models.CharField(max_length=20, choices=REGISTRATION_TYPES, default='HỌC MỚI')
    registration_date = models.DateTimeField(auto_now_add=True)
    term = models.CharField(max_length=20, verbose_name='Đợt đăng ký')

    class Meta:
        unique_together = ('student', 'course', 'term')
