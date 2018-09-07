from django.urls import path
from . import views

urlpatterns = [
	path('', views.catalog, name = 'catalog'),
	path('delete/<int:id>/', views.delete),
#	path('edit/<int:id>/', views.edit),
]