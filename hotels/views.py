from django.shortcuts import render
from .models import Hotel

# Create your views here.
def all_hotels(request):
    hotels = Hotel.objects.all()
    return render(request, "hotels.html", {"hotels": hotels})
