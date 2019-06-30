from django.urls import path, re_path
from testurlapp import views

urlpatterns = [
	#site.com/user/12/2000/
	path('user/<int:month>/<int:year>/', views.home, name='home'),
]