from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^mypassbook$',views.mypassbook,name='mypassbook')
]