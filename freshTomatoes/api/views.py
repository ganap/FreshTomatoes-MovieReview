from rest_framework import generics

from .serializers import UserSerializer, MovieSerializer

from .models import Movie
from .permissions import CanEditPermission
from rest_framework.views import APIView
from django.contrib.auth import login, logout
from rest_framework.response import Response
from . import serializers, permissions, authenticators
from django.http import Http404
from rest_framework import status

class MovieMixin(object):
    model = Movie
    serializer_class = MovieSerializer
    permission_classes = [
       CanEditPermission
    ]


class MovieList(MovieMixin, generics.ListCreateAPIView):
    pass

class MovieDetail(APIView):

    """
    Retrieve, update or delete a Movie instance.
    """

    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Movie = self.get_object(pk)
        serializer = MovieSerializer(Movie)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MovieSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def put(self, request, pk, format=None):
    #     Movie = self.get_object(pk)
    #     serializer = MovieSerializer(Movie, data=request.DATA)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Movie = self.get_object(pk)
        Movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AuthView(APIView):
    authentication_classes = (authenticators.QuietBasicAuthentication,)

    def post(self, request, *args, **kwargs):
        login(request, request.user)
        return Response(serializers.UserSerializer(request.user).data)

    def delete(self, request, *args, **kwargs):
        logout(request)
        return Response()
