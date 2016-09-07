from django.shortcuts import render
from .models import Location

def home(request):
    locations = Location.objects.all()
    return render(request, 'home.html', {'locations': locations})

def detail(request, location_id):
    locations = Location.objects.get(id=location_id)
    return render(request, 'detail.html', {'location': location})
