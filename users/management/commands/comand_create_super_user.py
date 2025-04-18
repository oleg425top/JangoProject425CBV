from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        admin_user = User.objects.create(
            email='admincbv@web.top',
            first_name='Admin',
            last_name='Adminov',
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )
        admin_user.set_password('querty123456')
        admin_user.save()
        print('ADmin Created!!')
