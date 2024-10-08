from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """
    Команда ввода суперюзера
    """

    def handle(self, *args, **options):
        user = User.objects.create(
            email="admin@sky.pro",
            first_name="Admin",
            last_name="SkyPro",
            is_staff=True,
            is_superuser=True,
        )

        user.set_password("123qwe456rty")
        user.save()
