from django.conf.urls import url
from home.views import HomeView
from . import views

urlpatterns = [
	url(r'^b2c/register/$', views.register, name='register'),
	url(r'^b2c-profile/$', views.view_b2c_profile, name='view_profile'),
    url(r'^b2c-profile/(?P<pk>\d+)/$', views.view_b2c_profile, name='view_b2c_profile_with_pk'),
    url(r'^b2c-profile/edit/$', views.edit_b2c_profile, name='edit_b2c_profile'),
	]