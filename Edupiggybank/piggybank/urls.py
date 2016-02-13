from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.passbook_list, name='passbook_list'),
]