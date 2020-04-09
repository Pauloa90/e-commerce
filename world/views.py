from django.shortcuts import render
<<<<<<< HEAD
from .models import Lugares


# Create your views here.
def all_continentes(request):
    """A view that display the index page"""
    todos = Lugares.objects.all()

    return render(request, "world.html", {"todos": todos})

=======
from .models import World

# Create your views here.
def all_world(request):
    worlds = Worlds.objects.all()
    return render(request, "worlds.html", {"worlds": worlds})
>>>>>>> b0e884ed60785b5910bda8bdecfbccd4688d3d85


