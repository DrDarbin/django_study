from django.urls import path, re_path
from testurlapp import views

urlpatterns = [
	re_path(r'^user/(\d+)/$', views.home, name='home'),
]