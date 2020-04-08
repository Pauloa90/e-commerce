from django.shortcuts import render
from .models import World

# Create your views here.
def all_world(request):
    worlds = Worlds.objects.all()
    return render(request, "worlds.html", {"worlds": worlds})


