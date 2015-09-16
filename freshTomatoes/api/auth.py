from django.contrib.auth.models import User


class AlwaysRootBackend(object):
    def authenticate(self, *args, **kwargs):
        """Always returns the `root` user.  DO NOT USE THIS IN PRODUCTION!"""
        return User.objects.get(username='superuser')

    def get_user(self, user_id):
        return User.objects.get(username='superuser')
