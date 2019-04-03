from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os


class Command(BaseCommand):

    def handle(self, *args, **options):
        username = os.environ.get('SU_NAME', 'admin')
        email = os.environ.get('SU_EMAIL', 'admin@example.com')
        password = os.environ.get('SU_PASSWORD', 'admin123')
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, email, password)
