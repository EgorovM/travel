from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^login/$', views.login, name = 'index'),
    url(r'^register/$', views.register, name = 'index'),
    url(r'^settings/$', views.settings, name = 'index'),
    url(r'^logout/$', views.logout_view, name = 'index'),
    url(r'^filter/$', views.filter, name = 'index'),
    url(r'^confirm/$', views.confirm, name = 'index'),
    url(r'^notifications/$', views.notifications, name = 'index'),
    url(r'^residents/$', views.residents, name = 'index'),
    url(r'^about/$', 		 views.about, name = 'index'),
    url(r'^profile/(?P<user_id>[0-9]+)/$', views.profile, name = 'index'),

    # url(r'^(?P<order_id>[0-9]+)/$', views.order, name='order'),
    # url(r'^login/$', views.login, name = 'login'),
]
