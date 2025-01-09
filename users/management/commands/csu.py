from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(email='admin@example.com', date_born='2000-01-01')
        user.set_password('123qwe')
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
