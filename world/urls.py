from django.conf.urls import url, include
from .views import all_continentes

urlpatterns = [
    url(r'^$/', all_continentes, name='world'),

]