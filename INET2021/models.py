from django.db import models

# Create your models here.

class Manager(models.Model):
    first_name = models.CharField(max_length=100, default=None)
    last_name = models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Time(models.Model):
    hour = models.TimeField(auto_created=True)
    cant = models.IntegerField(default=0)

    def __str__(self):
        return str(self.hour) + str(self.cant)

class Local(models.Model):
    name = models.CharField(max_length=100, default=None)
    max_cap = models.IntegerField()
    ac_cap = models.IntegerField()
    address = models.CharField(max_length=100, default=None)
    manager = models.ForeignKey(Manager, on_delete= models.CASCADE,blank=True)
    time = models.ManyToManyField(Time)

    def call_percentage(self):
        percentage = ((self.ac_cap * 100) / self.max_cap)
        return round(percentage)

    def __str__(self):
        return self.name

    def triggerAdd(self):
        if (self.ac_cap < self.max_cap):
            self.ac_cap += 1

        self.call_percentage()

    def triggerRemove(self):
        if (self.ac_cap != 0):
            self.ac_cap -= 1

        self.call_percentage()






