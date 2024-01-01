

from django.shortcuts import render,redirect

from Admin.views import place
from Condractor.views import constructorhome
from .models import*
from Admin.models import District,Place,Admin

def homepage(request):
    return render(request,"Guest/Home.html")

def newuser(request):
    dist=District.objects.all()
    if request.method=='POST':
        place=request.POST.get('Place')
        loc=Place.objects.get(id=place)
        Newuser.objects.create(Name=request.POST.get('txt_name'),Contact=request.POST.get('txt_contact'),
        Gender=request.POST.get('n3'),
        Email=request.POST.get('txt_email'),Place=loc,
        Address=request.POST.get('txt_address'),Password=request.POST.get('txt_password'))
        return render(request,"Guest/Thankyou.html")
    else:
        newuser=Newuser.objects.all()
        return render(request,"Guest/Newuser.html",{"distric":dist,"user":newuser})

def placeload(request):
    dist=request.GET.get('district')
    place=Place.objects.filter(District=dist)
    return render(request,'Guest/Placedropdown.html',{'place':place})



def newcondractor(request):
    dist=District.objects.all()
    if request.method=="POST" and request.FILES:
        place=request.POST.get('Place')
        loc=Place.objects.get(id=place)  
        NewConstructor.objects.create(Name=request.POST.get("txt_name"),Contact=request.POST.get('txt_contact'),
        Gender=request.POST.get('txt_gender'),Email=request.POST.get('txt_email'),
        Place=loc,Address=request.POST.get('txt_address'),Totalemployees=request.POST.get('txt_totalemployees'),
        Registeredname=request.POST.get('txt_registername'),Licensenumber=request.POST.get('txt_Licensenumber'),
        Proof1=request.FILES.get('image_Proof1'),Proof2=request.FILES.get('image_Proof2'),
        Password=request.POST.get('txt_password'))
        
        return render(request,"Guest/Thanksverify.html")
    else:
        newcon=NewConstructor.objects.all()
        return render(request,"Guest/Newcondractor.html",{"distric":dist,"newcon":newcon})


def newworker(request):
    dist=District.objects.all()
    if request.method=="POST"and request.FILES:
        place=request.POST.get('Place')
        loc=Place.objects.get(id=place)
        Newworker.objects.create(Name=request.POST.get('txt_name'),Contact=request.POST.get('txt_contact'),
        Gender=request.POST.get('n3'),Email=request.POST.get('txt_email'),
        Place=loc,Experience=request.POST.get('txt_experience'),
        Address=request.POST.get('txt_address'),Username=request.POST.get('txt_username'),
        Password=request.POST.get('txt_password'),Proofworker=request.FILES.get('image_Proof1'),title=request.POST.get("title"))
        return render(request,"Guest/Thankyou.html")
    else:
        newworker=Newworker.objects.all()
        return render(request,"Guest/Newworker.html",{"distric":dist,"newcon":newworker})





def Login(request):
    if request.method=='POST':
        username=request.POST.get("username")
        password=request.POST.get("password")
        newuserlog=Newuser.objects.filter(Email=username,Password=password).count()
        newconstructorlog1=NewConstructor.objects.filter(Email=username,Password=password).count()
        newworkerlog2=Newworker.objects.filter(Username=username,Password=password).count()
        newlandlordlog3=NewLandlord.objects.filter(Username=username,Password=password).count()
        Adminlog4=Admin.objects.filter(username=username,password=password).count()
        if newuserlog>0:
            newuser=Newuser.objects.get(Email=username,Password=password)
            request.session["userid"]=newuser.id
            return redirect("User:index")
        elif newconstructorlog1>0:
            newconst=NewConstructor.objects.get(Email=username,Password=password,construct_status='1')
            request.session["constructid"]=newconst.id
            return redirect("Condractor:index")

        elif newworkerlog2>0:
            newworker=Newworker.objects.get(Username=username,Password=password)
            request.session["newworkerid"]=newworker.id
            return redirect("Worker:index")

        elif newlandlordlog3>0:
            newlandlord=NewLandlord.objects.get(Username=username,Password=password,Newlandlor_status='1')
            request.session["newlandlordid"]=newlandlord.id
            return redirect("Landlord:index")


        elif Adminlog4>0:
            admin=Admin.objects.get(username=username,password=password)
            request.session["Adminid"]=admin.id
            return redirect("/Admin/home/")
        else:
            error="Invalid Details / Check UserName  or  Password"
            return render(request,"Guest/Login.html",{"error":error})
    else: 
         return render(request,"Guest/Login.html")



def Landlord(request):
    dist=District.objects.all()
    if request.method=="POST" and request.FILES:
        place=request.POST.get('Place')
        loc=Place.objects.get(id=place)  
        NewLandlord.objects.create(Name=request.POST.get("txt_Name"),Contact=request.POST.get('txt_Contact'),
        Email=request.POST.get('txt_email'),Proof=request.FILES.get('image_Proof'),Photo=request.FILES.get("image"),
        Place=loc,Address=request.POST.get('txt_Address'),Username=request.POST.get('txt_username'),
        Password=request.POST.get('txt_password'))
        return render(request,"Guest/Thanksverify.html")

    else:
        newlandlord=NewLandlord.objects.all()
        return render(request,"Guest/Newlandlord.html",{"distric":dist,"newlandlord":newlandlord})




def register(request):
    return render(request,"Guest/Registration.html")

def indexpage(request):
    return render(request,"Guest/index.html")


def about(request):
    return render(request,"Guest/about.html")


def contact(request):
    return render(request,"Guest/Contact.html")


def Thankyou(request):
    return render(request,"Guest/Thankyou.html")



def Thanksverify(request):
    return render(request,"Guest/Thanksverify.html")