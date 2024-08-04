from django.urls import path
from .views import TripViewSet
from .views import create_trip, list_trips, update_trip, delete_trip
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'trips', TripViewSet)
urlpatterns = [
    path('trips/<int:pk>/edit/', update_trip, name='update_trip'), 
    path('trips/<int:pk>/delete/', delete_trip, name='delete_trip'), 
]

urlpatterns += router.urls  
