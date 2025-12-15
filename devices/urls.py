from django.urls import path
from devices import views


app_name = 'devices'


urlpatterns = [
path('', views.device_list, name='device_list'),
path('create/', views.device_create, name='device_create'),
path('<int:pk>/', views.device_detail, name='device_detail'),
path('<int:pk>/action/', views.device_action, name='device_action'),