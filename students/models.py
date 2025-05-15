from django.db import models

class Student(models.Model):
    GENDER_CHOICES = [
        ('Nam', 'Nam'),
        ('Nữ', 'Nữ')
    ]
    EDUCATION_LEVEL_CHOICES = [
        ('Đại học', 'Đại học'),
        ('Cao đẳng', 'Cao đẳng'),
        ('Thạc sĩ', 'Thạc sĩ'),
        ('Tiến sĩ', 'Tiến sĩ')
    ]
    EDUCATION_TYPE_CHOICES = [
        ('Chính quy', 'Chính quy'),
        ('Liên thông', 'Liên thông'),
        ('Từ xa', 'Từ xa')
    ]

    student_id = models.CharField(max_length=20, unique=True, verbose_name='MSSV')
    full_name = models.CharField(max_length=200, verbose_name='Họ tên')
    class_name = models.CharField(max_length=50, verbose_name='Lớp học', default='DHKHDL17A')
    major = models.CharField(max_length=100, verbose_name='Ngành')
    academic_year = models.CharField(max_length=20, verbose_name='Khóa học', default='2021 - 2022')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, verbose_name='Giới tính')
    date_of_birth = models.DateField(verbose_name='Ngày sinh')
    place_of_birth = models.CharField(max_length=200, verbose_name='Nơi sinh')
    education_level = models.CharField(max_length=20, choices=EDUCATION_LEVEL_CHOICES, verbose_name='Bậc đào tạo')
    education_type = models.CharField(max_length=20, choices=EDUCATION_TYPE_CHOICES, verbose_name='Loại hình đào tạo')

    def __str__(self):
        return f"{self.student_id} - {self.full_name}"

    class Meta:
        ordering = ['student_id']
