from django.db import models

# Create your models here.
class Flavors(models.Model):
    name = models.TextField()
    price = models.TextField()
    type = models.TextField()

    def __str__(self):
        return "{} {}".format(self.name, self.price)

