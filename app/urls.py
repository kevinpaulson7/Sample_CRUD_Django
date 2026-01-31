from django.urls import path
from . import views

urlpatterns = [
    path('', views.bike_list, name='bike_list'),
    path('bikes/add/', views.bike_create, name='bike_create'),
    path('bikes/update/<int:id>/', views.bike_update, name='bike_update'),
    path('bikes/delete/<int:id>/', views.bike_delete, name='bike_delete'),
]
