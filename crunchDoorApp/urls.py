from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.home, name="home"),
	url(r'^companies/(?P<query>[\w-]+)/(?P<order>[\w-]+)$', views.index, name="index"),
	url(r'^new$', views.create, name="create"),
	# crunchDoorApp/5
	url(r'^company/(?P<company_id>[0-9]+)/$', views.detail,name='detail'),
	url(r'^company/(?P<company_id>[0-9]+)/update/$', views.update,name='update'),
	url(r'^company/(?P<company_id>[0-9]+)/delete/$', views.delete,name='delete'),

]