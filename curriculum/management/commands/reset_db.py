from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db import connection
from django.core.management import call_command
from curriculum.models import CurriculumFramework, SubjectGroup, Subject, Semester
from students.models import Student
from courses.models import Course, CourseRegistration
from datetime import datetime

class Command(BaseCommand):
    help = 'Reset database and add sample data'

    def handle(self, *args, **options):
        # Drop all tables
        with connection.cursor() as cursor:
            cursor.execute("PRAGMA foreign_keys = OFF;")
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            for table in tables:
                if table[0] != 'sqlite_sequence':
                    cursor.execute(f"DROP TABLE IF EXISTS {table[0]};")
            cursor.execute("PRAGMA foreign_keys = ON;")

        # Run migrations
        call_command('migrate')

        # Create superuser
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')

        # Add sample data
        # Curriculum Frameworks
        curriculum = CurriculumFramework.objects.create(
            name='Chương trình đào tạo Công nghệ thông tin',
            description='Chương trình đào tạo ngành Công nghệ thông tin',
            total_credits=150,
            is_active=True
        )

        # Semesters
        semester1 = Semester.objects.create(
            curriculum=curriculum,
            name='Học kỳ 1',
            order=1
        )
        semester2 = Semester.objects.create(
            curriculum=curriculum,
            name='Học kỳ 2',
            order=2
        )
        semester3 = Semester.objects.create(
            curriculum=curriculum,
            name='Học kỳ 3',
            order=3
        )

        # Subject Groups
        group1 = SubjectGroup.objects.create(
            semester=semester1,
            name='Kiến thức giáo dục đại cương',
            is_required=True,
            order=1
        )
        group2 = SubjectGroup.objects.create(
            semester=semester1,
            name='Kiến thức cơ sở ngành',
            is_required=True,
            order=2
        )
        group3 = SubjectGroup.objects.create(
            semester=semester2,
            name='Kiến thức chuyên ngành',
            is_required=True,
            order=1
        )

        # Subjects
        subject1 = Subject.objects.create(
            group=group1,
            name='Nhập môn lập trình',
            credits=3,
            theory_hours=30,
            practice_hours=30,
            is_required=True,
            order=1
        )
        subject2 = Subject.objects.create(
            group=group1,
            name='Cấu trúc dữ liệu và giải thuật',
            credits=4,
            theory_hours=45,
            practice_hours=30,
            is_required=True,
            order=2
        )
        subject3 = Subject.objects.create(
            group=group2,
            name='Cơ sở dữ liệu',
            credits=3,
            theory_hours=30,
            practice_hours=30,
            is_required=True,
            order=1
        )
        subject4 = Subject.objects.create(
            group=group3,
            name='Lập trình Web',
            credits=3,
            theory_hours=30,
            practice_hours=30,
            is_required=True,
            order=1
        )

        # Students
        student1 = Student.objects.create(
            student_id='SV001',
            full_name='Nguyễn Văn A',
            class_name='CNTT1',
            major='Công nghệ thông tin',
            academic_year='2023-2024',
            gender='Nam',
            date_of_birth='2000-01-01',
            place_of_birth='Hà Nội',
            education_level='Đại học',
            education_type='Chính quy'
        )
        student2 = Student.objects.create(
            student_id='SV002',
            full_name='Trần Thị B',
            class_name='CNTT1',
            major='Công nghệ thông tin',
            academic_year='2023-2024',
            gender='Nữ',
            date_of_birth='2000-02-02',
            place_of_birth='Hồ Chí Minh',
            education_level='Đại học',
            education_type='Chính quy'
        )

        # Courses
        course1 = Course.objects.create(
            course_id='INT1001',
            class_code='INT1001.1',
            name='Nhập môn lập trình',
            credits=3,
            is_mandatory=True,
            prerequisites='',
            term='2023-2024-1'
        )
        course2 = Course.objects.create(
            course_id='INT1002',
            class_code='INT1002.1',
            name='Cấu trúc dữ liệu và giải thuật',
            credits=4,
            is_mandatory=True,
            prerequisites='INT1001',
            term='2023-2024-1'
        )
        course3 = Course.objects.create(
            course_id='INT2001',
            class_code='INT2001.1',
            name='Cơ sở dữ liệu',
            credits=3,
            is_mandatory=True,
            prerequisites='INT1001',
            term='2023-2024-2'
        )
        course4 = Course.objects.create(
            course_id='INT3001',
            class_code='INT3001.1',
            name='Lập trình Web',
            credits=3,
            is_mandatory=True,
            prerequisites='INT1001',
            term='2023-2024-2'
        )

        # Course Registrations
        CourseRegistration.objects.create(
            student=student1,
            course=course1,
            registration_date=datetime.now(),
            status='registered'
        )
        CourseRegistration.objects.create(
            student=student1,
            course=course2,
            registration_date=datetime.now(),
            status='registered'
        )
        CourseRegistration.objects.create(
            student=student2,
            course=course1,
            registration_date=datetime.now(),
            status='registered'
        )
        CourseRegistration.objects.create(
            student=student2,
            course=course3,
            registration_date=datetime.now(),
            status='registered'
        )

        self.stdout.write(self.style.SUCCESS('Successfully reset database and added sample data')) 