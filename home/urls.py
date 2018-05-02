from django.conf.urls import url
from home.views import register, CompanyListView, CompanyDetail
from . import views

urlpatterns = [
    url(r'^$', views.register, name='home'),
    url(r'^api/$', CompanyListView.as_view()),
    url(r'^api/(?P<pk>[0-9]+)/$', views.CompanyDetail.as_view()),
    
]