from django.shortcuts import render,redirect
from Admin.models import Complainttype, District
from Admin.models import Landfactors

from Guest.models import NewLandlord
from Landlord.models import ManageLands,Landfacilities,LandGallery, landlordComplaint
from User.models import Feedback, LandBooking

# Create your views here.




def Landlorddetails(request):
    profile=NewLandlord.objects.get(id=request.session["newlandlordid"])
    return render(request,"Landlord/LandlordProfile.html",{"details":profile,})
    



def updateLandlrd(request,cid):
    Landlrdupd=NewLandlord.objects.get(id=cid)
    if request.method=="POST": 
       Landlrdupd.Name=request.POST.get("txt_name") 
       Landlrdupd.Address=request.POST.get("txt_address")
       Landlrdupd.Contact=request.POST.get("txt_contact")
       Landlrdupd.Email=request.POST.get("txt_email")
      
       Landlrdupd.save()
       return redirect('Landlord:View-Profile')

    else:
        return render(request,"Landlord/EditLandlord.html",{"Landlrdupd":Landlrdupd})



def changepassword(request,cid):
    chngpass=NewLandlord.objects.get(id=cid)
    psw=chngpass.Password
    if request.method=='POST':
        old=request.POST.get("txt_crrntpass")
        if old!=psw:
            Eror="Password Not Correct"
            return render(request,"Landlord/Changepassword.html",{"Error":Eror})
        else:
            new=request.POST.get("txt_newpass")
            chngpass=NewLandlord.objects.get(id=cid)
            chngpass.Password=new
            chngpass.save()
            #messages.success("password changed successfully..please login again")
            return redirect('Guest:Login')
    else:
        return render(request,"Landlord/Changepassword.html")


def managelandsoflord(request):
    dist=District.objects.all()
    if "newlandlordid" in request.session:
        land=NewLandlord.objects.get(id=request.session["newlandlordid"])
    
        if request.method=="POST" and request.FILES:
            manage=NewLandlord.objects.get(id=request.session["newlandlordid"])

            distid=request.POST.get("District")
            distobject=District.objects.get(id=distid)
            ManageLands.objects.create(Area=request.POST.get("txt_area"),Photo=request.FILES.get('image'),Landlord=manage,
            Rate=request.POST.get("txt_rate"),Pincode=request.POST.get("txt_pincode"),Location=request.POST.get("txt_location"),
            district=distobject)
            landid=ManageLands.objects.filter(Landlord=land)
            return render(request,"Landlord/Managelands.html",{"distric":dist,"landid":landid})
        else:
            landid=ManageLands.objects.filter(Landlord=land)
            print(landid)
            return render(request,"Landlord/Managelands.html",{"distric":dist,"landid":landid})
    else:
        return redirect('Guest:Login')



def landfacilities(request,cid):
    landfactt=Landfactors.objects.all()
    land=ManageLands.objects.get(id=cid)
    if request.method=='POST' and request.FILES:
        cid=request.POST.get("txt_facilities")
        landfac=Landfactors.objects.get(id=cid)
        Landfacilities.objects.create(Facilities=landfac,Discription=request.POST.get("txt_discription"),Land=land,Photo=request.FILES.get("image"))
        return render(request,"Landlord/Landfacilities.html")
    else:
        return render(request,"Landlord/Landfacilities.html",{"landfactt":landfactt,"land":land})


def landssgallery(request,cid):
    if "newlandlordid" in request.session:
        if request.method=='POST' and request.FILES:
            const=ManageLands.objects.get(id=cid)
            lndgal=LandGallery.objects.filter(managelands=cid)
            LandGallery.objects.create(Caption=request.POST.get("txt_caption"),Photo=request.FILES.get("image"),managelands=const)
            return render(request,"Landlord/LandGallery.html",{"landgal":lndgal})
        else:
            lndgal=LandGallery.objects.filter(managelands=cid)
            return render(request,"Landlord/LandGallery.html",{"landgal":lndgal})
    else:
        return redirect('Guest:Login')

def dltlndgallery(request,did):
    LandGallery.objects.get(id=did).delete()
    return redirect('Landlord:manageland')


def viewlandbook(request):
    if "newlandlordid" in request.session:
        landlord=NewLandlord.objects.get(id=request.session["newlandlordid"])
        mange=ManageLands.objects.filter(Landlord=landlord)
        for x in mange:

            land=LandBooking.objects.filter(manageland=x)
            return render(request,"Landlord/ViewLandBooking.html",{"land":land})
    else:
        return redirect('Guest:Login')

def acceptlandbooking(request,aid):
    verify=LandBooking.objects.get(id=aid)
    verify.b_status=True
    verify.save()
    return redirect ('Landlord:viewlandbook')

def landbookingreject(request,did):
    veri=LandBooking.objects.get(id=did)
    veri.b_status=False
    veri.save()
    return redirect ('Landlord:viewlandbook')




def indexpage(request):
    return render(request,"Landlord/index.html")


def Landfeedback(request):
    if "newlandlordid" in request.session:
        if request.method=='POST':
            Feedback.objects.create(Feedback=request.POST.get('landlordfeedback'))
            feed=Feedback.objects.all()
            return render(request,"Landlord/Landlordfeedback.html")
        else:
            feed=Feedback.objects.all()
            return render(request,"Landlord/Landlordfeedback.html",{'Feedback':feed})
    else:
        return redirect('guest:Login')


def Landcomplaint(request):
    if "newlandlordid" in request.session:
        
        landobj=NewLandlord.objects.get(id=request.session['newlandlordid'])
        comp=landlordComplaint.objects.filter(landlord=landobj)
        if request.method=='POST':
            landlordComplaint.objects.create(complaint=request.POST.get('complaint'),landlord=landobj)
            return render(request,"Landlord/LandlordCompllaint.html",{"comp":comp})
        else:
            

            return render(request,"Landlord/LandlordCompllaint.html",{"comp":comp,"Usrobj":landobj})
    else:
        return redirect('guest:Login')



def dlt(request,landlordid):
    NewLandlord.objects.get(id=landlordid).delete()
    return redirect('Guest:Login')