from django.urls import path
from Guest import views
from . import views
app_name='User'
urlpatterns = [
    
    path('ViewProfile/',views.userdetails,name="View-userProfile"),
    path('updateuser/<int:cid>/',views.updateuser,name="Updateuser"),
    path('changepassword/<int:cid>/',views.changepassword,name="changepassword"),
    path('searchconst/',views.constsearch,name="searchconst"),
    path('serchbytype/',views.searchpreviouswork,name="searchtype"),
    path('viewmoreperwrk/<int:pid>',views.viewmoreprvwork,name="viewmoreprv"),
    path('searchworker/',views.workersearch,name="searchworker"),
    path('viewmoresrchwork/<int:wid>',views.viewmoresearchwork,name="viewmoresrchwrk"),
    path('searchland/',views.Landsearch,name="searchland"),
    path('viewmorecondractor/<int:conid>',views.viewmoreconstructor,name="viewmoreconstructor"),
    path('token/<int:toid>',views.token,name="tokenpage"),
    path('viewbookedland/',views.viewbookedland,name="viewbookland"),
    path('payment/<int:pid>',views.payment,name="payment"),
    path('bookingworker/<int:wid>',views.bookingworker,name="workerbooking"),
    path('bookingconstructor/<int:cid>',views.bookingconst,name="constructurbooking"),
    path('viewConstructorstatus/',views.viewconstructorstatus,name="viewworkestatus"),
    path('vieworkerstatus/',views.viewworkerstatus,name="viewworkestatus"),
    path('Contact/<int:coid>',views.Contactworker,name="contactworker"),
    path('paymentworker/<int:pid>',views.paymentworker,name="paymentforworker"),
    path('balanceworker/<int:pid>',views.balanceworker,name="balanceforworker"),
    path('userfeedback/',views.userfeedback,name="UserFeedback"),
    path('index/',views.indexpage,name="index"),
    path('viewworksgallery/<int:vid>/',views.worksgallery,name='viewworksgal'),
    path('viewbookedworker/',views.viewbookedworker,name="viewbookdworker"),
    path('usercomplaints/',views.newcomplaint,name="UserComplaints"),
    path('Viewbookedconstructor/',views.viewbookedconstructor,name="viewbookedconst"),
    path('viewProfile/<int:aid>/',views.viewProfile,name="View-Profile"),
    path('viewLatest/<int:pid>/',views.viewLatest,name="View-Latest"),
    path('viewLand facilities/<int:aid>/',views.viewfacilities,name="Viewlandfacilities"),
    path('viewlandgallery/<int:aid>/',views.landgallery,name='viewgal'),
    path('deleteuser/<int:userid>',views.dlt,name="dltuser"),
    path('Viewphoto/<int:aiid>/',views.image,name="View"),
    
    



    




]