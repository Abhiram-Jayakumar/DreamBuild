from copyreg import constructor
from django.db import models
from Admin.models import Complainttype, Contractservice
from Guest.models import NewConstructor

# Create your models here.

class previouswork(models.Model):
    Type=models.ForeignKey(Contractservice,on_delete=models.SET_NULL,null=True)
    Squarefeet=models.CharField(max_length=20)
    Photo=models.FileField(upload_to="Previousworkimage/")
    Description=models.CharField(max_length=70)
    Totalamount=models.CharField(max_length=20)
    Duration=models.CharField(max_length=20)
    Condractor=models.ForeignKey(NewConstructor,on_delete=models.SET_NULL,null=True)


class WorksGallery(models.Model):
    Caption=models.CharField(max_length=20)
    Photo=models.FileField(upload_to="Worksgallery/")
    prevoius=models.ForeignKey(previouswork,on_delete=models.SET_NULL,null=True)


class consComplaint(models.Model):
    complaint=models.CharField(max_length=200)
    constructor=models.ForeignKey(NewConstructor,on_delete=models.SET_NULL,null=True,default=False)
    
    
    Complaint_Date=models.DateTimeField(auto_now=True)
    Complaintreply=models.CharField(max_length=200,default="No reply")
    Complaint_Status=models.IntegerField(default=False)
    complaint_type=models.ForeignKey(Complainttype,on_delete=models.SET_NULL,null=True)
    