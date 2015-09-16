from rest_framework import generics

from .serializers import UserSerializer, MovieSerializer

from django.contrib.auth.models import User
from .models import Movie
from .permissions import CanEditPermission
from . import serializers, permissions, authenticators


class UserList(generics.ListAPIView):
    model = User
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    model = User
    serializer_class = UserSerializer
    lookup_field = 'username'

    def get_permissions(self):
        # allow non-authenticated user to create
        return (permissions.AllowAny() if self.request.method == 'POST'
                else permissions.IsStaffUser()),


class MovieMixin(object):
    model = Movie
    serializer_class = MovieSerializer
    permission_classes = [
       CanEditPermission
    ]


class MovieDetail(MovieMixin, generics.RetrieveUpdateDestroyAPIView):
    pass


class MovieList(MovieMixin, generics.ListCreateAPIView):
    pass

