from django.conf.urls import urls, include
from .views import all_curiosities

urlspatterns = [
    urls(r'^$', all_curiosities, name='curiosities')
]