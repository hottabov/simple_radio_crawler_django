from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail'),

    url(r'^genries/$', views.genre_list, name='genre_list'),
    url(r'^genre/$', views.genre, name='genre'),

    url(r'^countries/$', views.country_list, name='country_list'),
    url(r'^country/$', views.country, name='country'),

    url(r'^cities/$', views.city_list, name='city_list'),
    url(r'^city/$', views.city, name='city'),  

    url(r'^bitrates/$', views.bitrate_list, name='bitrate_list'),
    url(r'^bitrate/$', views.bitrate, name='bitrate'),      
]