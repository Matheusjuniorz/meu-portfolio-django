import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

User = get_user_model()

if not User.objects.filter(username='matheus').exists():
    User.objects.create_superuser('matheus', 'batistam032@gmail.com', '22052002mj')
    print("Superusuário matheus criado com sucesso!")
else:
    print("Superusuário matheus já existe.")