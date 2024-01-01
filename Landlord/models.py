from django.db import models
from Admin.models import Complainttype, District,Landfactors
from Guest.models import NewLandlord

# Create your models here.
class ManageLands(models.Model):
    Area=models.CharField(max_length=30)
    Photo=models.FileField(upload_to="ManageLand/")
    Rate=models.CharField(max_length=10)
    district=models.ForeignKey(District,on_delete=models.SET_NULL,null=True)
    Pincode=models.CharField(max_length=20)
    Location=models.CharField(max_length=20)
    Landlord=models.ForeignKey(NewLandlord,on_delete=models.SET_NULL,null=True)


class Landfacilities(models.Model):
    Facilities=models.ForeignKey(Landfactors,on_delete=models.SET_NULL,null=True)
    Discription=models.CharField(max_length=50)
    Photo=models.FileField(upload_to="Landfacilities/")
    Land=models.ForeignKey(ManageLands,on_delete=models.SET_NULL,null=True)

class LandGallery(models.Model):
    Caption=models.CharField(max_length=20)
    Photo=models.FileField(upload_to="Landgallery/")
    managelands=models.ForeignKey(ManageLands,on_delete=models.SET_NULL,null=True)


class landlordComplaint(models.Model):
    complaint=models.CharField(max_length=200)
    landlord=models.ForeignKey(NewLandlord,on_delete=models.SET_NULL,null=True,default=False)
    
    
    Complaint_Date=models.DateTimeField(auto_now=True)
    Complaintreply=models.CharField(max_length=200,default="No reply")
    Complaint_Status=models.IntegerField(default=False)
    complaint_type=models.ForeignKey(Complainttype,on_delete=models.SET_NULL,null=True)
    