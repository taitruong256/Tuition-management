from django.db import models

# Create your models here.

class CurriculumFramework(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Semester(models.Model):
    curriculum = models.ForeignKey(CurriculumFramework, on_delete=models.CASCADE, related_name='semesters')
    name = models.CharField(max_length=50)  # Ví dụ: Học kỳ 1
    order = models.PositiveIntegerField(default=1)
    total_credits = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.curriculum.name} - {self.name}"

class SubjectGroup(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='groups')
    name = models.CharField(max_length=100, default='Nhóm bắt buộc')
    is_required = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.semester.name} - {self.name}"

class Subject(models.Model):
    group = models.ForeignKey(SubjectGroup, on_delete=models.CASCADE, related_name='subjects')
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50)
    credits = models.PositiveIntegerField(default=0)
    theory_hours = models.PositiveIntegerField(default=0)
    practice_hours = models.PositiveIntegerField(default=0)
    is_passed = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name
