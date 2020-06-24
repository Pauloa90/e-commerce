from django.conf.urls import url, include
from .views import all_hotels

urlpatterns = [
    url(r'^$', all_hotels, name='hotels')
]

