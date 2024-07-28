from django.urls import path
from . import views

urlpatterns = [
    path('trips/new/', views.create_trip, name='create_trip'),
    path('trips/', views.list_trips, name='list_trips'),
    path('trips/<int:pk>/edit/', views.update_trip, name='update_trip'),
    path('trips/<int:pk>/delete/', views.confirm_delete, name='confirm_delete'),
]