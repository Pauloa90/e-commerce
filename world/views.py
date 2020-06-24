from django.shortcuts import render
from .models import Lugares


# Create your views here.
def all_resorts(request):
    """A view that display the index page"""
    todos = Lugares.objects.all()

    return render(request, "world.html", {"todos": todos})