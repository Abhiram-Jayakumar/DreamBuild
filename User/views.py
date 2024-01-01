
from django.shortcuts import render,redirect

from django.db.models import Q

from Guest.models import NewConstructor, Newuser, Newworker
from Admin.models import Complainttype, District, Landfactors,Place,Contractservice
from Condractor.models import WorksGallery, previouswork
from Landlord.models import LandGallery, ManageLands,Landfacilities
from User.models import Complaint, Feedback, LandBooking, constructorbooking, newworkerbooking
from Worker.models import LatestWork, Workerprofile

# Create your views here.


def userdetails(request):
    profile=Newuser.objects.get(id=request.session["userid"])
    return render(request,"User/Userprofile.html",{"details":profile,})
    
    
def updateuser(request,cid):
    userupd=Newuser.objects.get(id=cid)
    if request.method=="POST" :
       userupd.Name=request.POST.get("txt_name") 
       userupd.Address=request.POST.get("txt_address")
       userupd.Contact=request.POST.get("txt_contact")
       userupd.Email=request.POST.get("txt_email")
       userupd.save()
       return redirect('User:View-userProfile')

    else:
        return render(request,"User/Edituser.html",{"userupd":userupd})


def changepassword(request,cid):
    chngpass=Newuser.objects.get(id=cid)
    psw=chngpass.Password
    if request.method=='POST':
        old=request.POST.get("txt_crrntpass")
        if old!=psw:
            Eror="Password Not Correct"
            return render(request,"User/Changepassword.html",{"Error":Eror})
        else:
            new=request.POST.get("txt_newpass")
            chngpass=Newuser.objects.get(id=cid)
            chngpass.Password=new
            chngpass.save()
            #messages.success("password changed successfully..please login again")
            return redirect('Guest:Login')
    else:
        return render(request,"User/Changepassword.html")


def placeload(request):
    dist=request.GET.get('district')
    place=Place.objects.filter(District=dist)
    return render(request,'Guest/Placedropdown.html',{'place':place})

def constsearch(request):
    if "userid" in request.session:

        dist=District.objects.all()
        if request.method=="POST":
            plcid=request.POST.get('txt_place')
            plce=Place.objects.get(id=plcid)
            const=NewConstructor.objects.filter(Place=plce)
            return render(request,"user/SearchConstructor.html",{"District":dist,"const":const})
        else:
            const=NewConstructor.objects.all()
            return render(request,"User/SearchConstructor.html",{"District":dist,"const":const})
    else:
        return redirect('Guest:Login')

def viewmoreconstructor(request,conid):
    if request.method=="POST":
        viewmorecon=NewConstructor.objects.filter(id=conid)
        return render(request,'User/ViewmoreConstructor.html',{"viewmorecon":viewmorecon})

    else:
        viewmorecon=NewConstructor.objects.filter(id=conid)
        return render(request,'User/ViewmoreConstructor.html',{"viewmorecon":viewmorecon})


def searchpreviouswork(request):
    if "userid" in request.session:
        wrktyp=Contractservice.objects.all()
        prevwork=previouswork.objects.all()
        # print(prevwork)
        if request.method=="POST":
           typid=request.POST.get("txt_type")
           type=Contractservice.objects.get(id=typid) 
           prevwork=previouswork.objects.filter(Type=type)
           return render(request,'User/Searchpreviouswork.html',{"wrkytp":wrktyp,"prevwork":prevwork})
        else:
            prevwork=previouswork.objects.all()

            return render(request,'User/Searchpreviouswork.html',{"wrkytp":wrktyp,"prevwork":prevwork})
    else:
        return redirect('Guest:Login')

    
def viewmoreprvwork(request,pid):
    if request.method=='POST':
        prevwork=previouswork.objects.filter(Condractor=pid)
        print(prevwork)
        return render(request,'User/Viewmorepreviouswork.html',{"prevwork":prevwork})
    else:
        prevwork=previouswork.objects.filter(Condractor=pid)
        print(prevwork)
        return render(request,'User/Viewmorepreviouswork.html',{"prevwork":prevwork})



def workersearch(request):
    if "userid" in request.session:

        dist=District.objects.all()
        if request.method=="POST":
            plcid=request.POST.get('txt_place')
            plce=Place.objects.get(id=plcid)
            Wrkrsrch=Newworker.objects.filter(Place=plce)
            return render(request,"user/SearchWorker.html",{"District":dist,"Wrkrsrch":Wrkrsrch})
        else:
            Wrkrsrch=Newworker.objects.all()
            return render(request,"User/SearchWorker.html",{"District":dist,"Wrkrsrch":Wrkrsrch})
    else:
        return redirect('Guest:Login')


def viewmoresearchwork(request,wid):
    if request.method=="POST":
        prevsrchwork=Newworker.objects.filter(id=wid)
        return render(request,'User/Viewmoreworker.html',{"prevsrchwork":prevsrchwork})

    else:
        prevsrchwork=Newworker.objects.filter(id=wid)
        return render(request,'User/Viewmoreworker.html',{"prevsrchwork":prevsrchwork})

def Landsearch(request):
    if "userid" in request.session:
        dist=District.objects.all()
        facil=Landfactors.objects.all()
        if request.method=="POST":
            distid=request.POST.get("txt_distict")
            disobj=District.objects.get(id=distid)
            landobj=ManageLands.objects.filter(district=disobj)
            return render(request,"user/SearchLand.html",{"dist":dist,"facil":facil,"data":landobj})
        else:
            landobj=ManageLands.objects.all()
            return render(request,"user/SearchLand.html",{"dist":dist,"facil":facil,"data":landobj})
    else:
        return redirect('Guest:Login')

def token(request,toid):
    if "userid" in request.session:
        toi=ManageLands.objects.get(id=toid)
        
        if request.method=="POST":
            userobj=Newuser.objects.get(id=request.session["userid"])
            LandBooking.objects.create(manageland=toi,User=userobj)
            land=LandBooking.objects.all()
            return render(request,'User/Tokenland.html',{"i":toi,"userobj":userobj,"land":land})
        else:
            toi=ManageLands.objects.get(id=toid)
            
            return render(request,'User/Tokenland.html',{"i":toi})
    else:
         return redirect('Guest:index')


def viewbookedland(request):    
    if "userid" in request.session:
        booked=LandBooking.objects.filter(User=request.session["userid"])
        return render (request,'User/ViewBookedLand.html',{"booked":booked})
    else:
         return redirect('Guest:index')

def payment(request,pid):
    if "userid" in request.session:
        pay=LandBooking.objects.get(id=pid)
        if request.method=='POST':
            hid=request.POST.get("hidden")
            pay=LandBooking.objects.get(id=hid)
            pay.p_status=True
            pay.save()
            return redirect('User:viewbookland')
        else:
            return render(request,"User/Payment.html",{"pay":pay})
    else:
        return redirect('Guest:Login')


def bookingconst(request,cid):
    if "userid" in request.session:
        toi=NewConstructor.objects.get(id=cid)  
        con1=NewConstructor.objects.filter(id=cid)      
        if request.method=='POST':
            details=request.POST.get("txt_details")
            print(details)
            da=request.POST.get("from_date")
            print(da)
            userobj=Newuser.objects.get(id=request.session["userid"])
            constructorbooking.objects.create(newConstructor=toi,User1=userobj,Details=details,Date=da)
            conb=constructorbooking.objects.all()
            return render(request,'User/Bookingconstructor.html',{"i":toi,"userobj":userobj,"conb":conb,"con1":con1})
        else:
            toi=NewConstructor.objects.get(id=cid)            
            return render(request,'User/Bookingconstructor.html',{"i":toi,"con1":con1})
    else:
         return redirect('User:index')




def bookingworker(request,wid):
    if "userid" in request.session:
        toi=Newworker.objects.get(id=wid)  
        wo1=Newworker.objects.filter(id=wid)      
        if request.method=='POST':
            details=request.POST.get("txt_details")
            print(details)
            da=request.POST.get("from_date")
            # print(da)
            userobj=Newuser.objects.get(id=request.session["userid"])
            newworkerbooking.objects.create(newworker=toi,User2=userobj,Details=details,Date=da)
            conb=newworkerbooking.objects.all()
            return render(request,'User/BookingWorker.html',{"i":toi,"userobj":userobj,"conb":conb,"wo1":wo1})
        else:
            toi=Newworker.objects.get(id=wid)            
            return render(request,'User/BookingWorker.html',{"i":toi,"wo1":wo1})
    else:
         return redirect('User:index')


def viewconstructorstatus(request):
    const1=constructorbooking.objects.all()
    return render(request,"User/viewConstructorStatus.html",{"const1":const1})

def viewworkerstatus(request):
    worksts=newworkerbooking.objects.all()
    return render(request,"User/ViewworkerStatus.html",{"worksts":worksts})



def Contactworker(request,coid):
    verify=newworkerbooking.objects.get(id=coid)
    print(verify)
    verify.p_status=1
    verify.save()
    return redirect ('User:viewbookdworker')



def paymentworker(request,pid):
    if "userid" in request.session:
        pay=newworkerbooking.objects.get(id=pid)
        if request.method=='POST':
            hid=request.POST.get("hidden")
            pay=newworkerbooking.objects.get(id=hid)
            pay.p_status=2
            pay.save()
            return redirect('User:viewbookdworker')
        else:
            return render(request,"User/Payment.html",{"pay":pay})
    else:
        return redirect('Guest:Login')

def balanceworker(request,pid):
    if "userid" in request.session:
        pay=newworkerbooking.objects.get(id=pid)
        if request.method=='POST':
            hid=request.POST.get("hidden")
            pay=newworkerbooking.objects.get(id=hid)
            pay.p_status=4
            pay.save()
            return redirect('User:viewbookdworker')
        else:
            return render(request,"User/Payment.html",{"pay":pay})
    else:
        return redirect('Guest:Login')




def userfeedback(request):
    if "userid" in request.session:
        if request.method=='POST':
            Feedback.objects.create(Feedback=request.POST.get('userfeedback'))
            feed=Feedback.objects.all()
            return render(request,"User/Userfeedback.html")
        else:
            feed=Feedback.objects.all()
            return render(request,"User/Userfeedback.html",{'Feedback':feed})
    else:
        return redirect('Guest:Login')




def indexpage(request):
    return render(request,"User/index.html")

def worksgallery(request,vid):
    if "userid" in request.session:
        
        wrksgal=WorksGallery.objects.filter(prevoius=vid)
        return render(request,"User/ViewworksGallery.html",{"wrksgal":wrksgal})
    else:
        return redirect('Guest:Login')



def viewbookedworker(request):    
    if "userid" in request.session:
        userobj=Newuser.objects.get(id=request.session["userid"])
        booked=newworkerbooking.objects.filter(User2=userobj)
        return render (request,'User/Viewbookedworker.html',{"booked":booked})
    else:
         return redirect('Guest:index')





def newcomplaint(request):
    if "userid" in request.session:
        cmptype=Complainttype.objects.all()
        userobj=Newuser.objects.get(id=request.session['userid'])
        comp=Complaint.objects.filter(user=userobj)
        if request.method=='POST':
            typeob=request.POST.get('complaint_type')
            type=Complainttype.objects.get(id=typeob)

            Complaint.objects.create(complaint=request.POST.get('complaint'),complaint_type=type,user=userobj)
            return render(request,"User/UserCompllaint.html",{"comp":comp})
        else:
            cmptype=Complainttype.objects.all()

            return render(request,"User/UserCompllaint.html",{"CmpType":cmptype,"comp":comp,"Usrobj":userobj})
    else:
        return redirect('Guest:Login')




def viewbookedconstructor(request):    
    if "userid" in request.session:
        booked=constructorbooking.objects.filter(User1=request.session["userid"])
        
        return render (request,'User/ViewBoookedconstructor.html',{"booked":booked})
    else:
         return redirect('Guest:Login')

def viewProfile(request,aid):
    if "userid" in request.session:
        work=Workerprofile.objects.filter(newwrkr=aid)
        return render(request,'User/ViewWorkerProfile.html',{"work":work})
    else:
         return redirect('Guest:Login')

def viewLatest(request,pid):
    if "userid" in request.session:
        work=LatestWork.objects.filter(latest=pid)
        return render(request,'User/WorkerLatest.html',{"work":work})
    else:
         return redirect('Guest:Login')

def viewfacilities(request,aid):
    landonj=ManageLands.objects.get(id=aid)
    result=Landfacilities.objects.filter(Land=landonj)
    return render(request,"User/viewlandFacilities.html",{"result":result})


def landgallery(request,aid):
    if "userid" in request.session:
        landonj=ManageLands.objects.get(id=aid)
        landgal=LandGallery.objects.filter(managelands=landonj)
        return render(request,"User/ViewLandGallery.html",{"landgal":landgal})
    else:
        return redirect('Guest:Login')


def dlt(request,userid):
    Newuser.objects.get(id=userid).delete()
    return redirect('Guest:Login')



def image(request,aiid):
    if "userid" in request.session:
        
        wrksgal=LandGallery.objects.get(id=aiid)
        return render(request,"User/ViewPhoto.html",{"landgal":wrksgal})
    else:
        return redirect('Guest:Login')