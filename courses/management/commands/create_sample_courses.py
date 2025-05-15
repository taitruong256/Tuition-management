from django.core.management.base import BaseCommand
from courses.models import Course

class Command(BaseCommand):
    help = 'Creates sample courses for testing'

    def handle(self, *args, **kwargs):
        courses_data = [
            {
                'course_id': '2101409',
                'class_code': '4203000942',
                'name': 'Cấu trúc dữ liệu và giải thuật',
                'credits': 4,
                'is_mandatory': True,
                'term': 'HK3 (2024 - 2025)'
            },
            {
                'course_id': '2101402',
                'class_code': '4203000901',
                'name': 'Cấu trúc rời rạc',
                'credits': 3,
                'is_mandatory': True,
                'term': 'HK3 (2024 - 2025)'
            },
            {
                'course_id': '2112014',
                'class_code': '4203014167',
                'name': 'Chủ nghĩa xã hội khoa học',
                'credits': 2,
                'is_mandatory': True,
                'term': 'HK3 (2024 - 2025)'
            },
            {
                'course_id': '2101679',
                'class_code': '4203014064',
                'name': 'Đại số tuyến tính tính toán',
                'credits': 3,
                'is_mandatory': True,
                'term': 'HK3 (2024 - 2025)'
            },
            {
                'course_id': '2120501',
                'class_code': '4203003242',
                'name': 'Giáo dục Quốc phòng và An ninh 1',
                'credits': 4,
                'is_mandatory': True,
                'term': 'HK3 (2024 - 2025)'
            }
        ]

        for course_data in courses_data:
            Course.objects.get_or_create(
                course_id=course_data['course_id'],
                defaults=course_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully created sample courses'))
