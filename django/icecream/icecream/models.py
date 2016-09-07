from django.db import models

# By default, Django gives each model an auto-incrementing primary key field.
# id = models.AutoField(primary_key=True)
# locations = Location.objects.get(id=1)
class Location(models.Model):
    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)
