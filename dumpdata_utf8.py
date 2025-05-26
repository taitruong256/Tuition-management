import subprocess

with open('sample_data.json', 'w', encoding='utf-8') as f:
    subprocess.run(
        ['python', 'manage.py', 'dumpdata', 'accounts', 'curriculum', 'registration', 'debt', '--indent', '2'],
        stdout=f
    )