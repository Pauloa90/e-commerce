from django.conf.urls import url, include
<<<<<<< HEAD
from .views import all_continentes

urlpatterns = [
    url(r'^$/', all_continentes, name='world'),

]
=======
from .views import all_world

urlpatterns = [
    url(r'^$', all_world, name='world'),

]
>>>>>>> b0e884ed60785b5910bda8bdecfbccd4688d3d85
