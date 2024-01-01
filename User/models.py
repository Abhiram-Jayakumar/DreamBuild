from typing import NewType
from django.db import models
from Admin.models import Complainttype
from Guest.models import NewConstructor, NewLandlord, Newuser, Newworker
from Landlord.models import ManageLands

# Create your models here.
class LandBooking(models.Model):
    manageland=models.ForeignKey(ManageLands,on_delete=models.SET_NULL,null=True)
    Booking_Date=models.DateField(auto_now=True)
    b_status=models.IntegerField(default=False)
    p_status=models.IntegerField(default=False)
    User=models.ForeignKey(Newuser,on_delete=models.SET_NULL,null=True)

class constructorbooking(models.Model):
    newConstructor=models.ForeignKey(NewConstructor,on_delete=models.SET_NULL,null=True)
    Booking1_Date=models.DateField(auto_now=True)
    Date=models.DateField(auto_now=True)
    Details=models.CharField(max_length=30,null=True)
    b1_status=models.IntegerField(default=False)
    User1=models.ForeignKey(Newuser,on_delete=models.SET_NULL,null=True)


class newworkerbooking(models.Model):
    newworker=models.ForeignKey(Newworker,on_delete=models.SET_NULL,null=True)
    Booking2_Date=models.DateField(auto_now=True)
    Date=models.DateField()
    Details=models.CharField(max_length=30,null=True)
    b2_status=models.IntegerField(default=False)
    p_status=models.IntegerField(default=False)
    User2=models.ForeignKey(Newuser,on_delete=models.SET_NULL,null=True)
    constructor1=models.ForeignKey(NewConstructor,on_delete=models.SET_NULL,null=True)



class Complaint(models.Model):
    complaint=models.CharField(max_length=200)
    user=models.ForeignKey(Newuser,on_delete=models.SET_NULL,null=True,default=False)
    
    
    Complaint_Date=models.DateTimeField(auto_now=True)
    Complaintreply=models.CharField(max_length=200,default="No reply",null=True)
    Complaint_Status=models.IntegerField(default=False)
    complaint_type=models.ForeignKey(Complainttype,on_delete=models.SET_NULL,null=True)
    


class Feedback(models.Model):
    Feedback=models.CharField(max_length=200)
    Feedback_Date=models.DateTimeField(auto_now=True)




