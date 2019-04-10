from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    # url(r'^(?P<order_id>[0-9]+)/$', views.order, name='order'),
    # url(r'^login/$', views.login, name = 'login'),
]
