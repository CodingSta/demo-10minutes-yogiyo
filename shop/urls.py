from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^category/(?P<pk>\d+)/$', views.category_detail, name='category_detail'),
    url(r'^(?P<pk>\d+)/$', views.shop_detail, name='shop_detail'),
    url(r'^(?P<pk>\d+)/review/new/$', views.review_new, name='review_new'),
    url(r'^(?P<shop_pk>\d+)/order/new/$', views.order_new, name='order_new'),
    url(r'^(?P<shop_pk>\d+)/order/(?P<pk>\d+)/pay/$', views.order_pay, name='order_pay'),
]

