from django.conf.urls import url, include
from .views import all_world

urlpatterns = [
    url(r'^$', all_world, name='world'),

]
