import django
import os
import sys
import json

print("Script bắt đầu chạy...")

try:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tuition_management.settings')
    django.setup()

    from django.core.serializers import serialize
    from accounts.models import StudentUser
    from curriculum.models import Curriculum, Semester, Subject
    from registration.models import Room, Lecturer, ClassSubject, Registration
    from debt.models import TuitionDebt, OtherFee

    data = []

    def add_model(model, name):
        objs = model.objects.all()
        print(f"{name}: {objs.count()} bản ghi")
        data.extend(json.loads(serialize('json', objs)))

    add_model(StudentUser, "StudentUser")
    add_model(Curriculum, "Curriculum")
    add_model(Semester, "Semester")
    add_model(Subject, "Subject")
    add_model(Room, "Room")
    add_model(Lecturer, "Lecturer")
    add_model(ClassSubject, "ClassSubject")
    add_model(Registration, "Registration")
    add_model(TuitionDebt, "TuitionDebt")
    add_model(OtherFee, "OtherFee")

    with open('sample_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("Đã xuất dữ liệu ra sample_data.json thành công!")

except Exception as e:
    print("Lỗi:", e)