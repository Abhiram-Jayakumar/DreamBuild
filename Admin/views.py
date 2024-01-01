from django.shortcuts import render,redirect
from Condractor.models import consComplaint

from Guest.models import NewConstructor, NewLandlord, Newuser, Newworker
from Landlord.models import landlordComplaint
from User.models import Complaint, Feedback
from Worker.models import workerComplaint
from .models import *


def district(request):
    if request.method=='POST':
        District.objects.create(District_name=request.POST.get('txt_district'))
        dist=District.objects.all()
        return render(request,"Admin/District.html",{'Dist':dist})
    else:
        dist=District.objects.all()
        return render(request,"Admin/District.html",{'Dist':dist})

def districtdelete(request,uid):
    District.objects.get(id=uid).delete()
    return redirect('Admin:District')


def districtupdate(request,uid):
    selectdistric= District.objects.get(id=uid)
    if request.method=="POST":
        selectdistric.District_name=request.POST.get("txt_district")
        selectdistric.save()
        return redirect('Admin:District')  
    else:
        return render(request,"Admin/Editdist.html",{'sel_dist':selectdistric})

def place(request):
    dist=District.objects.all()
    if request.method=="POST":
        distid=request.POST.get("District")
        distobject=District.objects.get(id=distid)
        Place.objects.create(District=distobject,Place_name=request.POST.get("txt_place"),Pincode=request.POST.get("txt_pincode"))
        plc=Place.objects.all()
        return render(request,"Admin/Place.html",{"dist":dist,"plc":plc})
    else:
        plc=Place.objects.all()
        return render(request,"Admin/Place.html",{"dist":dist,"plc":plc})

def Placedelete(request,uid):
    Place.objects.get(id=uid).delete()
    return redirect('Admin:place')
    
def Placeupdate(request,uid):
    selectplace=Place.objects.get(id=uid)
    pls=District.objects.all()
    if request. method=='POST':
        distid=request.POST.get("District")
        distobject=District.objects.get(id=distid)
        selectplace.District=distobject
        selectplace.Place_name=request.POST.get("txt_place")
        selectplace.Pincode=request.POST.get("txt_pincode")
        selectplace.save()
        return redirect('Admin:place')
    else:
        return render(request,"Admin/Editplace.html",{'sel_place':selectplace,"pls":pls})

def workcategory(request):
    if request.method=='POST':
        Workcategory.objects.create(category=request.POST.get("txt_category"))
        wrk=Workcategory.objects.all()
        return render(request,"Admin/Workcategory.html",{"wrkc":wrk})
    else:
        wrk=Workcategory.objects.all()
        return render(request,"Admin/Workcategory.html",{"wrkc":wrk})
    
def workcategorydelete(request,uid):
    Workcategory.objects.get(id=uid).delete()
    return redirect('Admin:work')

def workcategoryupdate(request,uid):
    selectworkcategory= Workcategory.objects.get(id=uid)
    if request.method=='POST':
        selectworkcategory.category=request.POST.get("txt_category")
        selectworkcategory.save()
        return redirect('Admin:work')

    else:
        return render(request,"Admin/Editworkcategory.html",{'select':selectworkcategory})

def landfactors(request):
    if request.method=='POST':
        Landfactors.objects.create(Landfactors=request.POST.get("txt_landfactors"))
        lnd=Landfactors.objects.all()
        return render(request,"Admin/Landfactors.html",{'lnds':lnd})
    else:
        lnd=Landfactors.objects.all()
        return render(request,"Admin/Landfactors.html",{'lnds':lnd})

def landfactorsdelete(request,uid):
    Landfactors.objects.get(id=uid).delete()
    return redirect('Admin:Land')

def landfactorsupdate(request,uid):
    selectlandfactors= Landfactors.objects.get(id=uid)
    if request.method=='POST':
        selectlandfactors.category=request.POST.get("txt_landfactors")
        selectlandfactors.save()
        return redirect('Admin:Land')
    else:
        return render(request,"Admin/Editlandfactors.html",{'self':selectlandfactors})    


def complaintype(request):
    if request.method=='POST':
        Complainttype.objects.create(Complaint_Type=request.POST.get("txt_complainttype"))
        comp=Complainttype.objects.all()
        return render(request,"Admin/Complainttype.html",{'Comps':comp})
    else:
        comp=Complainttype.objects.all()
        return render(request,'Admin/Complainttype.html',{'Comps':comp})


def complaintdelete(request,uid):
    Complainttype.objects.get(id=uid).delete()
    return redirect('Admin:complaint')

def complaintsupdate(request,uid):
    selectlcomplaint=Complainttype.objects.get(id=uid)
    if request.method=='POST':
        selectlcomplaint. Complaint_Type=request.POST.get("txt_complainttype")
        selectlcomplaint.save()
        return redirect('Admin:complaint')
    else:
        return render(request,"Admin/Editcomplainttype.html",{'self':selectlcomplaint})


def condractservice(request):
    if request.method=='POST':
        Contractservice.objects.create(Service=request.POST.get("txt_service"))
        con=Contractservice.objects.all()
        return render(request,"Admin/Condractservice.html",{'Cons':con})
    else:
        con=Contractservice.objects.all()
        return render(request,'Admin/Condractservice.html',{'Cons':con})


def contactservicedelete(request,uid):
    Contractservice.objects.get(id=uid).delete()
    return redirect('Admin:Condract')

def contractserviceupdate(request,uid):
    selectlcondract=Contractservice.objects.get(id=uid)
    if request.method=='POST':
        selectlcondract.Service=request.POST.get("txt_service")
        selectlcondract.save()
        return redirect('Admin:Condract')
    else:
        return render(request,"Admin/EditCondractservice.html",{'selc':selectlcondract})

def viewuserdetails(request):
    result=Newuser.objects.all()
    return render(request,"Admin/Viewuser.html",{"result":result})

def viewnewconstuctor(request):
    view=NewConstructor.objects.all()
    return render(request,"Admin/Viewconstructor.html",{"view":view})

def constructoraccept(request,aid):
    verify=NewConstructor.objects.get(id=aid)
    verify.construct_status=True
    verify.save()
    return redirect ('Admin:viewconstructor')


def constructorreject(request,did):
    veri=NewConstructor.objects.get(id=did)
    veri.construct_status=False
    veri.save()
    return redirect ('Admin:viewconstructor')

def viewworker(request):
    result=Newworker.objects.all()
    return render(request,"Admin/Viewworker.html",{"result":result})

def Adminhome(request):
    return render(request,"Admin/AdminHome.html")




def viewlandlord(request):
    view=NewLandlord.objects.all()
    return render(request,"Admin/ViewLandLord.html",{"view":view})


def accept(request,lid):
    verify=NewLandlord.objects.get(id=lid)
    verify.Newlandlor_status=True
    verify.save()
    return redirect ('Admin:viewlandlord')


def reject(request,rid):
    veri=NewLandlord.objects.get(id=rid)
    veri.Newlandlor_status='2'
    veri.save()
    return redirect ('Admin:viewlandlord')



def allfeedbacks(request):
    viewfeed=Feedback.objects.all()
    return render(request,"Admin/AllFeedbacks.html",{'ViewFeedbacks':viewfeed})



def indexpage(request):
    return render(request,"Admin/index-admin.html")

def usercomp(request):
    comp=Complaint.objects.all()
    return render(request,'Admin/Usercomplaint.html',{"comp":comp})


def Replay(request,cid):
    comp=Complaint.objects.get(id=cid)
    if request.method=='POST':
        reply=request.POST.get("txt_rply")
        comp.Complaintreply=reply
        comp.Complaint_Status=1
        comp.save()
        return redirect('Admin:user-complaint')
    else:
        return render(request,'Admin/UsercomplaintRepaly.html',{"comp":comp})



def workercomp(request):
    comp=workerComplaint.objects.all()
    return render(request,'Admin/workercomplaint.html',{"comp":comp})


def workerReplay(request,wid):
    comp=workerComplaint.objects.get(id=wid)
    if request.method=='POST':
        reply=request.POST.get("txt_rply")
        comp.Complaintreply=reply
        comp.Complaint_Status=1
        comp.save()
        return redirect('Admin:worker-complaint')
    else:
        return render(request,'Admin/workerReply.html',{"comp":comp})


def conscomp(request):
    comp=consComplaint.objects.all()
    return render(request,'Admin/Constructorcomplaint.html',{"comp":comp})


def consReplay(request,wid):
    comp=consComplaint.objects.get(id=wid)
    if request.method=='POST':
        reply=request.POST.get("txt_rply")
        comp.Complaintreply=reply
        comp.Complaint_Status=1
        comp.save()
        return redirect('Admin:cons-complaint')
    else:
        return render(request,'Admin/constructorreply.html',{"comp":comp})

def landcomp(request):
    comp=landlordComplaint.objects.all()
    return render(request,'Admin/LandlordComplaint.html',{"comp":comp})


def landReplay(request,wid):
    comp=landlordComplaint.objects.get(id=wid)
    if request.method=='POST':
        reply=request.POST.get("txt_rply")
        comp.Complaintreply=reply
        comp.Complaint_Status=1
        comp.save()
        return redirect('Admin:land-complaint')
    else:
        return render(request,'Admin/LandlordReply.html',{"comp":comp})