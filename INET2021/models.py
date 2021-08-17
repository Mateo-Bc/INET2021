from django.db import models

# Create your models here.

class Local(models.Model):
    nomvre = models.CharField(max_length=100, default=None)
    max_cap = models.IntegerField()
    ac_cap = models.IntegerField()

    def sum_hernesto(self):
        if (self.ac_cap < self.max_cap):
            self.ac_cap += 1
        else:
            print("nashen't")

    def res_carlos(self):
        if (self.ac_cap != 0):
            self.ac_cap -= 1
        else:
            print("flashaste una banda man")

class Time(models.Model):
    date = models.DateField()



