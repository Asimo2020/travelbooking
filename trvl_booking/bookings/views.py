# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Trip
from .forms import TripForm

def create_trip(request):
    if request.method == 'POST':
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
    if request.method == 'POST':
        form = TripForm(request.POST, instance=trip)
        if form.is_valid():
            form.save()
            return redirect('list_trips')
    else:
        form = TripForm(instance=trip)
    return render(request, 'update_trip.html', {'form': form})

def confirm_delete(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    if request.method == 'POST':
        trip.delete()
        return redirect('list_trips')
    return render(request, 'confirm_delete.html', {'trip': trip})