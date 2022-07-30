from _ast import Or

from django.db import models

# Create your models here.

class Organization(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name=models.CharField(max_length=50)
    last_name =models.CharField(max_length=100)
    organization = models.ForeignKey(Organization,
                                     models.SET_NULL,
                                     blank=True,
                                     null=True, )

    def __str__(self):
        return "%s, %s" %(self.last_name, self.first_name)
