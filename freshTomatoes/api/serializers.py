from rest_framework import serializers

from django.contrib.auth.models import User
from .models import Movie


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', )


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
