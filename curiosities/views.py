from django.shortcuts import render

# Create your views here.
def all_curiosities(request):
    return render(request, "curiosities.html")