from django.urls import path, re_path
from . import views

urlpatterns = [
	path('', views.catalog, name = 'catalog'),
	path('delete/<int:id>/', views.delete),
	path('edit/<int:id>/', views.edit),
	#re_path(r'^(?P<sort>(?:\d{1,2}\.)+)', views.catalog_sorted),
	
]