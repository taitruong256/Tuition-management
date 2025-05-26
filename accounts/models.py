from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class StudentUserManager(BaseUserManager):
    def create_user(self, student_id, email, password=None, **extra_fields):
        if not student_id:
            raise ValueError('Student ID is required')
        if not email:
            raise ValueError('Email is required')
        
        email = self.normalize_email(email)
        user = self.model(student_id=student_id, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, student_id, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(student_id, email, password, **extra_fields)

class StudentUser(AbstractBaseUser, PermissionsMixin):
    student_id = models.CharField(max_length=10, unique=True, verbose_name='Mã số sinh viên')
    email = models.EmailField(unique=True, verbose_name='Email')
    full_name = models.CharField(max_length=100, verbose_name='Họ tên')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(max_length=10, choices=[('Nam', 'Nam'), ('Nữ', 'Nữ'), ('Khác', 'Khác')], verbose_name='Giới tính', blank=True, null=True)
    status = models.CharField(max_length=20, choices=[('Đang học', 'Đang học'), ('Tốt nghiệp', 'Tốt nghiệp'), ('Bảo lưu', 'Bảo lưu')], verbose_name='Trạng thái', blank=True, null=True)
    class_name = models.CharField(max_length=100, verbose_name='Lớp', blank=True, null=True)
    major = models.CharField(max_length=100, verbose_name='Ngành', blank=True, null=True)
    faculty = models.CharField(max_length=100, verbose_name='Khoa', blank=True, null=True)
    specialization = models.CharField(max_length=100, verbose_name='Chuyên ngành', blank=True, null=True)
    course_year = models.CharField(max_length=20, verbose_name='Khóa', blank=True, null=True)
    education_level = models.CharField(max_length=50, verbose_name='Bậc đào tạo', blank=True, null=True)
    education_type = models.CharField(max_length=50, verbose_name='Loại hình đào tạo', blank=True, null=True)
    campus = models.CharField(max_length=100, verbose_name='Cơ sở', blank=True, null=True)
    curriculum = models.ForeignKey('curriculum.Curriculum', on_delete=models.SET_NULL, null=True, blank=True, related_name='students', verbose_name='Chương trình khung')

    objects = StudentUserManager()

    USERNAME_FIELD = 'student_id'
    REQUIRED_FIELDS = ['email', 'full_name']

    def __str__(self):
        return f"{self.student_id} - {self.full_name}"

    class Meta:
        verbose_name = 'Sinh viên'
        verbose_name_plural = 'Sinh viên'
