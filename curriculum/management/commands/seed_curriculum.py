from django.core.management.base import BaseCommand
from curriculum.models import CurriculumFramework, Semester, SubjectGroup, Subject

class Command(BaseCommand):
    help = 'Seed default curriculum data'

    def handle(self, *args, **kwargs):
        # Tạo chương trình khung
        cf = CurriculumFramework.objects.create(name='Chương trình khung CNTT', description='Khung ngành Công nghệ thông tin')

        # Học kỳ 1
        hk1 = Semester.objects.create(curriculum=cf, name='Học kỳ 1', order=1, total_credits=11)
        group1 = SubjectGroup.objects.create(semester=hk1, name='Học phần bắt buộc', is_required=True, order=1)
        Subject.objects.create(group=group1, name='Nhập môn Tin học', code='4203002009', credits=2, theory_hours=30, practice_hours=0, is_passed=True, order=1)
        Subject.objects.create(group=group1, name='Kỹ năng làm việc nhóm', code='4203003192', credits=2, theory_hours=30, practice_hours=0, is_passed=True, order=2)
        Subject.objects.create(group=group1, name='Giáo dục Quốc phòng và An ninh 1', code='4203003242', credits=4, theory_hours=60, practice_hours=0, is_passed=True, order=3)
        Subject.objects.create(group=group1, name='Toán cao cấp 1', code='4203003259', credits=2, theory_hours=30, practice_hours=0, is_passed=True, order=4)
        Subject.objects.create(group=group1, name='Giáo dục thể chất 1', code='4203003307', credits=2, theory_hours=0, practice_hours=60, is_passed=True, order=5)
        Subject.objects.create(group=group1, name='Nhập môn Lập trình', code='4203003848', credits=2, theory_hours=0, practice_hours=60, is_passed=True, order=6)
        Subject.objects.create(group=group1, name='Triết học Mác - Lênin', code='4203014164', credits=3, theory_hours=45, practice_hours=0, is_passed=True, order=7)
        Subject.objects.create(group=group1, name='Chứng chỉ Tiếng Anh', code='4203015216', credits=0, theory_hours=0, practice_hours=0, is_passed=True, order=8)

        # Học kỳ 2
        hk2 = Semester.objects.create(curriculum=cf, name='Học kỳ 2', order=2, total_credits=12)
        # Có thể thêm dữ liệu cho các học kỳ tiếp theo nếu muốn

        self.stdout.write(self.style.SUCCESS('Seeded curriculum data successfully!')) 