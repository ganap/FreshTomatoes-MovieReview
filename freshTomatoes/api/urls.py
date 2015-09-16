from django.conf.urls import patterns, url, include

from .api import UserList, UserDetail
from .views import MovieList, MovieDetail
from .views import AuthView

user_urls = patterns('',
                     url(r'^/(?P<username>[0-9a-zA-Z_-]+)$', UserDetail.as_view(), name='user-detail'),
                     url(r'^$', UserList.as_view(), name='user-list')
                     )

movie_urls = patterns('',
                      url(r'^$', MovieList.as_view(), name='movie-list'),
                      url(r'^/(?P<pk>\d+)$', MovieDetail.as_view(), name='movie-detail'),
                      )

urlpatterns = patterns('',
                       url(r'^users', include(user_urls)),
                       url(r'^movies', include(movie_urls)),
                       url(r'^auth/$', AuthView.as_view(), name='authenticate')
                       )

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]