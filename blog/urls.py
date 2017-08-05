from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.blog_list, name='blog_list'),
    url(r'^(?P<pk>\d+)/$', views.blog_detail, name='blog_detail'),
    url(r'^new/$', views.crawler_new, name='crawler_new'),
    url(r'^profile/$', views.profile, name='profile'),
]