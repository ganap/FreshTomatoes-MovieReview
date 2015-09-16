from django.core.management.base import BaseCommand

from django.contrib.auth.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = ['Bob', 'Sally', 'Joe', 'Rachel']
        for user in users:
            username = user.lower()
            user = User.objects.create(username=username, email="{}@freshtomatoes.com".format(username),
                                       first_name=user)
            user.is_staff = True
            user.password = "{}123".format(username)
            user.set_password("secret")
            user.save()
