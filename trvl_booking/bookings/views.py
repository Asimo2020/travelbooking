from django.shortcuts import render, get_object_or_404, redirect
from .models import Trip
from .forms import TripForm
from rest_framework import viewsets
from .serializers import TripSerializer

def create_trip(request):
    if request.method == "POST":
        form = TripForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_trips')
    else:
        form = TripForm()
    return render(request, 'create_trip.html', {'form': form})

def list_trips(request):
    trips = Trip.objects.all()
    return render(request, 'list_trips.html', {'trips': trips})

def update_trip(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    if request.method == "POST":
        form = TripForm(request.POST, instance=trip)
        if form.is_valid():
            form.save()
            return redirect('list_trips')
    else:
        form = TripForm(instance=trip)
    return render(request, 'update_trip.html', {'form': form})

def delete_trip(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    if request.method == "POST":
        trip.delete()
        return redirect('list_trips')
    return render(request, 'confirm_delete.html', {'trip': trip})
class TripViewSet(viewsets.ModelViewSet):
    serializer_class = TripSerializer
    queryset = Trip.objects.all()