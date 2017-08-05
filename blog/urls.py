from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.blog_list, name='blog_list'),
    url(r'^new/$', views.crawler_new, name='crawler_new'),
    url(r'^(?P<pk>\d+)/edit/$', views.blog_edit, name='blog_edit'),
    url(r'^(?P<pk>\d+)/delete/$', views.blog_delete, name='blog_delete'),
    url(r'^(?P<pk>\d+)/$', views.blog_detail, name='blog_detail'),
    url(r'^profile/$', views.profile, name='profile'),
]