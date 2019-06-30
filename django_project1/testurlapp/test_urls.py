from django.urls import path, re_path
from testurlapp import views

urlpatterns = [
	#site.com/user/12/2000/
	re_path(r'^user/(\d{2})/(\d{4})/$', views.home, name='home'),
]