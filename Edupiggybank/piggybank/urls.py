from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^mypassbook$',views.mypassbook,name='mypassbook'),
    url(r'^transaction$',views.transaction,name='transaction'),
    url(r'^transaction/(?P<pk>[0-9]+)/$', views.transaction_detail, name='transaction_detail'),
    url(r'^transaction/(?P<pk>[0-9]+)/edit/$', views.transaction_edit, name='transaction_edit'),
    url(r'^login$',views.login,name='login'),
    url(r'^quiz$',views.quiz,name='quiz'),
    url(r'^result$',views.result,name='result'),
]