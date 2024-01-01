from unicodedata import category
from django.db import models
from Admin.models import Place

class Newuser(models.Model):
    Name=models.CharField(max_length=30)
    Contact=models.CharField(max_length=30)
    Gender=models.CharField(max_length=20)
    Email=models.EmailField(unique=True)
    Place=models.ForeignKey(Place,on_delete=models.SET_NULL,null=True)
    Address=models.TextField(unique=True)
    Password=models.CharField(unique=True,max_length=20)



class NewConstructor(models.Model):
    Name=models.CharField(max_length=30)
    Contact=models.CharField(max_length=30)
    Gender=models.CharField(max_length=20,null=False)
    Email=models.EmailField(max_length=100,unique=True)
    Place=models.ForeignKey(Place,on_delete=models.SET_NULL,null=True)
    Address=models.TextField(max_length=50)
    Totalemployees=models.CharField(max_length=20)
    Registeredname=models.CharField(max_length=20)
    Licensenumber=models.CharField(max_length=20)
    Proof1=models.FileField(upload_to="identyprrof1/")
    Proof2=models.FileField(upload_to="identyproof2/")
    Password=models.CharField(unique=True,max_length=20)
    construct_status=models.IntegerField(default=False)
    

class Newworker(models.Model):
    Name=models.CharField(max_length=30)
    Contact=models.CharField(max_length=30)
    Gender=models.CharField(max_length=20)
    Email=models.EmailField(unique=True)
    Place=models.ForeignKey(Place,on_delete=models.SET_NULL,null=True)
    Experience=models.CharField(max_length=30)
    title=models.CharField(max_length=30,null=True)
    Address=models.TextField(max_length=50)
    Username=models.CharField(max_length=30)
    Password=models.CharField(unique=True,max_length=20)
    worker_bookingstatus=models.IntegerField(default=False,null=True)
    Proofworker=models.FileField(upload_to="identyworker/",null=True)
    


class NewLandlord(models.Model):
    Name=models.CharField(max_length=30)
    Contact=models.CharField(max_length=30)
    Email=models.EmailField(unique=True)
    Address=models.TextField(max_length=50)
    Photo=models.FileField(upload_to="Landlordimage/")
    Place=models.ForeignKey(Place,on_delete=models.SET_NULL,null=True)
    Proof=models.FileField(upload_to="identyproofLandlord/")
    Username=models.CharField(max_length=30)
    Password=models.CharField(unique=True,max_length=20)
    Newlandlor_status=models.IntegerField(default=False)

