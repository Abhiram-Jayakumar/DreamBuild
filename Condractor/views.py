from pyexpat.errors import messages

from django.shortcuts import redirect, render
from Admin.models import Complainttype, Contractservice, District, Place, Workcategory
from Guest.models import NewConstructor, Newworker
from Condractor. models import consComplaint, previouswork,WorksGallery
from User.models import Complaint, Feedback, constructorbooking, newworkerbooking
from Worker.models import LatestWork, Workerprofile

# Create your views here.
def constructorhome (request):
     return render(request,"Condractor/Constructorhome.html")


def constructordetails(request):
    if "constructid" in request.session:
        profile=NewConstructor.objects.get(id=request.session["constructid"])
       
        return render(request,"Condractor/ViewProfile.html",{"Constructordetails":profile})
    else:
        constructordetails=NewConstructor.objects.all()
        return render(request,"Condractor/ViewProfile.html",{"Constructordetails":profile})
    
def updateconst(request,cid):
    constupd=NewConstructor.objects.get(id=cid)
    if request.method=="POST" :
       constupd.Name=request.POST.get("txt_name") 
       constupd.Address=request.POST.get("txt_address")
       constupd.Contact=request.POST.get("txt_contact")
       constupd.Email=request.POST.get("txt_email")
       constupd.save()
       return redirect('Condractor:View-Profile')

    else:
        return render(request,"Condractor/Editconstuctor.html",{"constupd":constupd})


def changepassword(request,cid):
    chngpass=NewConstructor.objects.get(id=cid)
    psw=chngpass.Password
    if request.method=='POST':
        old=request.POST.get("txt_crrntpass")
        if old!=psw:
            Eror="Password Not Correct"
            return render(request,"Condractor/Changepassword.html",{"Error":Eror})
        else:
            new=request.POST.get("txt_newpass")
            chngpass=NewConstructor.objects.get(id=cid)
            chngpass.Password=new
            chngpass.save()
            #messages.success("password changed successfully..please login again")
            return redirect('Guest:Login')
    else:
        return render(request,"Condractor/Changepassword.html")



def Previouswork(request):
    contract=Contractservice.objects.all()
    if "constructid" in request.session:
        if request.method=='POST' and request.FILES:
            prevwork=NewConstructor.objects.get(id=request.session["constructid"])
            cid=request.POST.get("Type")
            const=Contractservice.objects.get(id=cid)

            previouswork.objects.create(Type=const,Squarefeet=request.POST.get("txt_squarefeet"),Condractor=prevwork,
            Photo=request.FILES.get("image"),Description=request.POST.get("txt_discription"),
            Totalamount=request.POST.get("txt_totalamount"),Duration=request.POST.get("txt_duration"))
            
            prfconst=previouswork.objects.filter(Condractor=request.session["constructid"])
            return render(request,"Condractor/Previousworks.html",{"contract":contract,"prfconst":prfconst})
        else:
            prfconst=previouswork.objects.filter(Condractor=request.session["constructid"])
            return render(request,"Condractor/Previousworks.html",{"contract":contract,"prfconst":prfconst})
    else:
        return redirect('Guest:Login')



def worksgallery(request,cid):
    if "constructid" in request.session:
        if request.method=='POST' and request.FILES:
            const=previouswork.objects.get(id=cid)
            wrksgal=WorksGallery.objects.filter(prevoius=cid)
            WorksGallery.objects.create(Caption=request.POST.get("txt_caption"),Photo=request.FILES.get("image"),prevoius=const)
            return render(request,"Condractor/Worksgallery.html",{"wrksgal":wrksgal})
        else:
            wrksgal=WorksGallery.objects.filter(prevoius=cid)
            return render(request,"Condractor/Worksgallery.html",{"wrksgal":wrksgal})
    else:
        return redirect('Guest:Login')

def dltwrksgallery(request,did):
    WorksGallery.objects.get(id=did).delete()
    return redirect('Condractor:previous')

def viewprvwork(request):
    prfconst=previouswork.objects.all()
    return render(request,"Condractor/viewpreviuouswork.html",{"prfconst":prfconst})

def viewworksgallery (request,vid):
    wrksgal=WorksGallery.objects. all()
    return render(request,"Condractor/Viewworksgallery.html",{"wrksgal":wrksgal})


def viewconstbook(request):
   const1=constructorbooking.objects.filter(b1_status='0')
   return render(request,"Condractor/ViewconstBooking.html",{"const1":const1})

def acceptconstbooking(request,aid):
    verify=constructorbooking.objects.get(id=aid)
    print("Hello")
    verify.b1_status=True
    verify.save()
    return redirect ('Condractor:viewconstbook')

def landconstreject(request,did):
    veri=constructorbooking.objects.get(id=did)
    veri.b1_status=False
    veri.save()
    return redirect ('Condractor:viewconstbook')


def indexpage(request):
    return render(request,"Condractor/index.html")

def condractorfeedback(request):
    if "constructid" in request.session:
        if request.method=='POST':
            Feedback.objects.create(Feedback=request.POST.get('userfeedback'))
            feed=Feedback.objects.all()
            return render(request,"Condractor/condractorfeedback.html")
        else:
            feed=Feedback.objects.all()
            return render(request,"Condractor/condractorfeedback.html",{'Feedback':feed})
    else:
        return redirect('Guest:Login')


def Concomplaint(request):
    if "constructid" in request.session:
        cmptype=Complainttype.objects.all()
        conobj=NewConstructor.objects.get(id=request.session['constructid'])
        comp=consComplaint.objects.filter(constructor=conobj)
        if request.method=='POST':
            typeob=request.POST.get('complaint_type')
            type=Complainttype.objects.get(id=typeob)

            consComplaint.objects.create(complaint=request.POST.get('complaint'),complaint_type=type,constructor=conobj)
            return render(request,"Condractor/CondractorCompllaint.html",{"comp":comp})
        else:
            cmptype=Complainttype.objects.all()

            return render(request,"Condractor/CondractorCompllaint.html",{"CmpType":cmptype,"comp":comp,"Usrobj":conobj})
    else:
        return redirect('Guest:Login')



def dlt(request,consid):
    NewConstructor.objects.get(id=consid).delete()
    return redirect('Guest:Login')

def workersearch(request):
    if "constructid" in request.session:

        dist=District.objects.all()
        if request.method=="POST":
            plcid=request.POST.get('txt_place')
            plce=Place.objects.get(id=plcid)
            Wrkrsrch=Newworker.objects.filter(Place=plce)
            return render(request,"Condractor/SearchWorker.html",{"District":dist,"Wrkrsrch":Wrkrsrch})
        else:
            Wrkrsrch=Newworker.objects.all()
            return render(request,"Condractor/SearchWorker.html",{"District":dist,"Wrkrsrch":Wrkrsrch})
    else:
        return redirect('Guest:Login')


def viewmoresearchwork(request,wid):
    if request.method=="POST":
        prevsrchwork=Newworker.objects.filter(id=wid)
        return render(request,'Condractor/Viewmoreworker.html',{"prevsrchwork":prevsrchwork})

    else:
        prevsrchwork=Newworker.objects.filter(id=wid)
        return render(request,'Condractor/Viewmoreworker.html',{"prevsrchwork":prevsrchwork})


def viewProfile(request,aid):
    if "constructid" in request.session:
        work=Workerprofile.objects.filter(newwrkr=aid)
        return render(request,'Condractor/ViewWorkerProfile.html',{"work":work})
    else:
         return redirect('guest:Login')


def viewLatest(request,pid):
    if "constructid" in request.session:
        work=LatestWork.objects.filter(latest=pid)
        return render(request,'Condractor/WorkerLatest.html',{"work":work})
    else:
         return redirect('guest:Login')


def bookingworker(request,wid):
    if "constructid" in request.session:
        toi=Newworker.objects.get(id=wid)  
        wo1=Newworker.objects.filter(id=wid)      
        if request.method=='POST':
            details=request.POST.get("txt_details")
            print(details)
            da=request.POST.get("from_date")
            # print(da)
            userobj=NewConstructor.objects.get(id=request.session["constructid"])
            newworkerbooking.objects.create(newworker=toi,constructor1=userobj,Details=details,Date=da)
            conb=newworkerbooking.objects.all()
            return render(request,'Condractor/BookingWorker.html',{"i":toi,"userobj":userobj,"conb":conb,"wo1":wo1})
        else:
            toi=Newworker.objects.get(id=wid)            
            return render(request,'Condractor/BookingWorker.html',{"i":toi,"wo1":wo1})
    else:
         return redirect('Condractor:index')


def viewbookedworker(request):    
    if "constructid" in request.session:
        userobj=NewConstructor.objects.get(id=request.session["constructid"])
        booked=newworkerbooking.objects.filter(constructor1=userobj)
        return render (request,'Condractor/Viewbookedworker.html',{"booked":booked})
    else:
         return redirect('guest:index')

def paymentworker(request,pid):
    if "constructid" in request.session:
        pay=newworkerbooking.objects.get(id=pid)
        if request.method=='POST':
            hid=request.POST.get("hidden")
            pay=newworkerbooking.objects.get(id=hid)
            pay.p_status=2
            pay.save()
            return redirect('Condractor:viewbookdworker')
        else:
            return render(request,"User/Payment.html",{"pay":pay})
    else:
        return redirect('guest:Login')

def Contactworker(request,coid):
    verify=newworkerbooking.objects.get(id=coid)
    print(verify)
    verify.p_status=1
    verify.save()
    return redirect ('Condractor:viewbookdworker')

def balanceworker(request,pid):
    if "constructid" in request.session:
        pay=newworkerbooking.objects.get(id=pid)
        if request.method=='POST':
            hid=request.POST.get("hidden")
            pay=newworkerbooking.objects.get(id=hid)
            pay.p_status=4
            pay.save()
            return redirect('Condractor:viewbookdworker')
        else:
            return render(request,"User/Payment.html",{"pay":pay})
    else:
        return redirect('guest:Login')