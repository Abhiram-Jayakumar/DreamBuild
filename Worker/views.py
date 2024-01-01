from django.shortcuts import render,redirect
from Admin.models import Complainttype, Workcategory

from Guest.models import Newuser, Newworker
from User.models import Complaint, Feedback, newworkerbooking
from Worker.models import Workerprofile,LatestWork, workerComplaint

# Create your views here.
def workerhome (request):
     return render(request,"Worker/Workerhome.html")

def workerdetails(request):
    profile=Newworker.objects.get(id=request.session["newworkerid"])
    return render(request,"Worker/Viewworker.html",{"workerdetails":profile,})
    
    
def updateworker(request,wid):
    wrkupd=Newworker.objects.get(id=wid)
    if request.method=="POST" :
       wrkupd.Name=request.POST.get("txt_name") 
       wrkupd.Address=request.POST.get("txt_address")
       wrkupd.Contact=request.POST.get("txt_contact")
       wrkupd.Email=request.POST.get("txt_email")
       wrkupd.save()
       return redirect('Worker:View-workerProfile')

    else:
        return render(request,"Worker/Editworker.html",{"wrkupd":wrkupd})


def changepassword(request,wid):
    chngpass=Newworker.objects.get(id=wid)
    psw=chngpass.Password
    if request.method=='POST':
        old=request.POST.get("txt_crrntpass")
        if old!=psw:
            Eror="Password Not Correct"
            return render(request,"Worker/Changepassword.html",{"Error":Eror})
        else:
            new=request.POST.get("txt_newpass")
            chngpass=Newworker.objects.get(id=wid)
            chngpass.Password=new
            chngpass.save()
            return redirect('Guest:Login')
    else:
        return render(request,"Worker/Changepassword.html")

def workpofile(request):
    work=Workcategory.objects.all()
    if "newworkerid" in request.session:
        if request.method=='POST':
            workerid=Newworker.objects.get(id=request.session["newworkerid"])
            wid=request.POST.get("txt_Category")
            wrk=Workcategory.objects.get(id=wid)
            Workerprofile.objects.create(Category=wrk,Rate=request.POST.get("txt_rate"),newwrkr=workerid,
            Discription=request.POST.get("txt_discription"),Experience=request.POST.get("txt_experience"))
            prfwork=Workerprofile.objects.filter(newwrkr=request.session["newworkerid"])
            return render(request,"Worker/Addwork.html",{"work":work,"prfwork":prfwork})

        else:
            prfwork=Workerprofile.objects.filter(newwrkr=request.session["newworkerid"])
            return render(request,"Worker/Addwork.html",{"work":work,"prfwork":prfwork})
    else:
        return redirect('Guest:Login')

def Latestwork(request,wid):
    if "newworkerid" in request.session:
        if request.method=="POST" and request.FILES:
            wrk=Workerprofile.objects.get(id=wid)
            LatestWork.objects.create(Title=request.POST.get("txt_title"),Description=request.POST.get("txt_description"),
            Photo=request.FILES.get('image'),latest=wrk)
            result=LatestWork.objects.filter(latest=wid)
            return render(request,"Worker/Latestwork.html",{"result":result})
        else:
            result=LatestWork.objects.filter(latest=wid)
            return render(request,"Worker/Latestwork.html",{"result":result})


def viewworkerbook(request):
    
    const1=newworkerbooking.objects.filter(newworker=request.session["newworkerid"])
    return render(request,"Worker/Viewworkerbooking.html",{"const1":const1})

def acceptworkerbooking(request,waid):
    verify=newworkerbooking.objects.get(id=waid)
    print(verify)
    aid=verify.newworker.id
    workobj=Newworker.objects.get(id=aid)
    print(workobj)
    workobj.worker_bookingstatus=1
    verify.b2_status=True
    verify.save()
    workobj.save()
    return redirect ('Worker:viewworkerbook')

def rejectworkerbooking(request,wdid):
    veri=newworkerbooking.objects.get(id=wdid)
    aid=veri.newworker.id
    workobj=Newworker.objects.get(id=aid)
    print(workobj)
    workobj.worker_bookingstatus=0
    veri.b2_status=False
    veri.save()
    workobj.save()
    return redirect ('Worker:viewworkerbook')



def workcomplete(request,wcoid):
    verify=newworkerbooking.objects.get(id=wcoid)
    print(verify)
    aid=verify.newworker.id
    workobj=Newworker.objects.get(id=aid)
    print(workobj)
    workobj.worker_bookingstatus=0
    verify.p_status=2
    verify.save()
    workobj.save()
    
    return redirect ('Worker:viewworkerbook')



def indexpage(request):
    return render(request,"Worker/index.html")



def workerfeedback(request):
    if "newworkerid" in request.session:
        if request.method=='POST':
            Feedback.objects.create(Feedback=request.POST.get('userfeedback'))
            feed=Feedback.objects.all()
            return render(request,"Worker/Workerfeedback.html")
        else:
            feed=Feedback.objects.all()
            return render(request,"Worker/Workerfeedback.html",{'Feedback':feed})
    else:
        return redirect('guest:Login')



def newcomplaint(request):
    if "newworkerid" in request.session:
        
        workerobj=Newworker.objects.get(id=request.session['newworkerid'])
        comp=workerComplaint.objects.filter(worker=workerobj)
        if request.method=='POST':
            workerComplaint.objects.create(complaint=request.POST.get('complaint'),worker=workerobj)
            return render(request,"Worker/workerCompllaint.html",{"comp":comp,"Usrobj":workerobj})
        else:
            return render(request,"Worker/workerCompllaint.html",{"comp":comp,"Usrobj":workerobj})
    else:
        return redirect('guest:Login')


def dlt(request,workerid):
    Newworker.objects.get(id=workerid).delete()
    return redirect('Guest:Login')
