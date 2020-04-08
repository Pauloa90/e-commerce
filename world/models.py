from django.db import models


# Create your models here.
class World(models.Model):
    place = models.CharField(max_length=254, default='')
    image = models.ImageField(upload_to='images_places')

    def __str__(self):
        return self.place