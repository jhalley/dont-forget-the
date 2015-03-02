from django.conf.urls import patterns, url
from grocery import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    
    # api stuff
    url(r'^api/list/$', views.list, name='list'),
    url(r'^api/list/(?P<list_id>\d*)/$', views.list, name='list'),
)