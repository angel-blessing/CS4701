from django.urls import path
from . import views
from . import xyproject3

urlpatterns = [
	path('', views.index, name='index'),
	path('splitDoc', views.splitDoc, name='splitDoc'),
	path('getAnswer', views.getAnswer, name='getAnswer'),
	path('init', xyproject3.init, name='init'),
]