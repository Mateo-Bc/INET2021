from django.db import models

# Create your models here.

class Local(models.Model):
    max_cap = models.IntegerField()
    ac_cap = models.IntegerField()

class Tiempo():
    date = models.DateField()



