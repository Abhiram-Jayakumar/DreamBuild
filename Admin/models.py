from unicodedata import category
from django.db import models

# Create your models here.
class District(models.Model):
    District_name=models.CharField(max_length=20)

    def __str__(self):
        return self.District_name


class Place(models.Model):
    District=models.ForeignKey(District,on_delete=models.CASCADE)
    Place_name=models.CharField(max_length=20)
    Pincode=models.CharField(max_length=20)

    def __str__(self):
       return self.Place_name

class Workcategory(models.Model):
    category=models.CharField(max_length=20)

    def __str__(self):
       return self.category


class Landfactors(models.Model):
    Landfactors=models.CharField(max_length=20)

    def __str__(self):
     return self.Landfactors


class Complainttype(models.Model):
    Complaint_Type=models.CharField(max_length=20)

    def __str__(self):
      return self.Complaint_Type


class Contractservice(models.Model):
    Service=models.CharField(max_length=20)

    def __str__(self):
     return self.Service

class Admin(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)