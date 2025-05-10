from django.core.management import BaseCommand

from users.models import User, UserRols




class Command(BaseCommand):

    def handle(self, *args, **options):
        admin = User.objects.create(
            email='admincbv@web.top',
            first_name='Admin',
            last_name='Adminov',
            role=UserRols.ADMIN,
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )
        admin.set_password('querty123456')
        admin.save()
        print('Admin Created!!')

        moderator = User.objects.create(
            email='moderator@web.top',
            first_name='Moderator',
            last_name='Moderatorov',
            role=UserRols.MODERATOR,
            is_staff=True,
            is_superuser=False,
            is_active=True,
        )
        moderator.set_password('querty123456')
        moderator.save()
        print('Moderator Created!!')


        user = User.objects.create(
            email='user@web.top',
            first_name='User',
            last_name='Userov',
            role=UserRols.USER,
            is_staff=True,
            is_superuser=False,
            is_active=True,
        )
        user.set_password('querty123456')
        user.save()
        print('User Created!!')
