from django.db import models
from Admin.models import Complainttype, Workcategory
from Guest.models import Newworker

# Create your models here.

class Workerprofile(models.Model):
    Category=models.ForeignKey(Workcategory,on_delete=models.SET_NULL,null=True)
    Rate=models.CharField(max_length=20)
    Discription=models.CharField(max_length=50)
    Experience=models.CharField(max_length=50)
    newwrkr=models.ForeignKey(Newworker,on_delete=models.SET_NULL,null=True)

class LatestWork(models.Model):
    Title=models.CharField(max_length=50)
    Description=models.CharField(max_length=50)
    Photo=models.FileField(upload_to="Latestwork/")
    latest=models.ForeignKey(Workerprofile,on_delete=models.SET_NULL,null=True)


class workerComplaint(models.Model):
    complaint=models.CharField(max_length=200)
    worker=models.ForeignKey(Newworker,on_delete=models.SET_NULL,null=True,default=False)
    
    
    Complaint_Date=models.DateTimeField(auto_now=True)
    Complaintreply=models.CharField(max_length=200,default="No reply")
    Complaint_Status=models.IntegerField(default=False)
    complaint_type=models.ForeignKey(Complainttype,on_delete=models.SET_NULL,null=True)
    