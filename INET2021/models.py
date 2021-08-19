from django.db import models

# Create your models here.

class Manager(models.Model):
    nomvre = models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.nomvre

class Local(models.Model):
    nomvre = models.CharField(max_length=100, default=None)
    max_cap = models.IntegerField()
    ac_cap = models.IntegerField()
    address = models.CharField(max_length=100, default=None)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE, null=True)

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



