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

    def cal_percentage(self):
        percentage = self.ac_cap / self.max_cap
        return percentage

    def __str__(self):
        return self.nomvre

    def sum_hernesto(self):
        if (self.ac_cap < self.max_cap):
            self.ac_cap += 1
        else:
            print("nashen't")
        self.cal_percentage()

    def res_carlos(self):
        if (self.ac_cap != 0):
            self.ac_cap -= 1
        else:
            print("flashaste una banda man")
        self.cal_percentage()


class Time(models.Model):
    date = models.DateField()



