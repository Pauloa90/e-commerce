from django.conf.urls import url, include
from .views import all_resorts

urlpatterns = [
    url(r'^$/', all_resorts, name='world'),

]
