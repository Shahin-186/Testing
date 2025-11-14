from django.urls import path
from . import views

app_name = 'dealership'

urlpatterns = [
    path('', views.home, name='home'),
    path('cars/', views.CarListView.as_view(), name='car_list'),
    path('cars/<int:pk>/', views.CarDetailView.as_view(), name='car_detail'),
]
