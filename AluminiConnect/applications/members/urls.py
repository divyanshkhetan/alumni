from django.conf.urls import url

from . import views

app_name = 'members'

urlpatterns = [
    url(r'(?P<year>[0-9]{4})/(?P<branch>[A-Z]+)/$', views.branch, name="branch"),
    url(r'(?P<year>[0-9]{4})/$', views.batch, name="batch"),
    url(r'^$', views.index, name='index'),
]