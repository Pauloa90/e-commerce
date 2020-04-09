from django.db import models

<<<<<<< HEAD
# Create your models here.
class Lugares(models.Model):
    continente = models.CharField(max_length=254, default='')
    imagens = models.ImageField(upload_to='images')

    def __str__(self):
        return self.continente
=======

# Create your models here.
class World(models.Model):
    place = models.CharField(max_length=254, default='')
    image = models.ImageField(upload_to='images_places')

    def __str__(self):
        return self.place
>>>>>>> b0e884ed60785b5910bda8bdecfbccd4688d3d85
