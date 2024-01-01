from django.urls import path
from Condractor import views
app_name='Condractor'
urlpatterns = [
    path('Constructorhome/',views.constructorhome,name="constructorhomepage"),
    path('ViewProfile/',views.constructordetails,name="View-Profile"),
    path('updateconstructor/<int:cid>/',views.updateconst,name="Update"),
    path('changepassword/<int:cid>/',views.changepassword,name="changepassword"),
    path('previous/',views.Previouswork,name="previous"),
    path('worksgallery/<int:cid>/',views.worksgallery,name='worksgal'),
    path('deletewrkgallery/<int:did>/',views.dltwrksgallery,name="dltworksgallery"),
    path('Viewpreviouswork/',views.viewprvwork,name="View-prv"),
    path('viewworksgallery/<int:vid>/',views.viewworksgallery,name='viewworksgal'),
    path('viewconstbooking/',views.viewconstbook,name="viewconstbook"),
    path('acceptconstbooking/<int:aid>/',views.acceptconstbooking,name="accept"),
    path('rejectconstbooking/<int:did>/',views.landconstreject,name="reject"),
    path('index/',views.indexpage,name="index"),
    path('condractorfeedback/',views.condractorfeedback,name="CondractorFeedback"),
    path('concomplaints/',views.Concomplaint,name="Complaintscondractor"),
    path('deleteconstructor/<int:consid>',views.dlt,name="dltcons"),
    path('searchworker/',views.workersearch,name="searchworker"),
    path('viewmoresrchwork/<int:wid>',views.viewmoresearchwork,name="viewmoresrchwrk"),
    path('viewProfile/<int:aid>/',views.viewProfile,name="View-Profile"),
    path('viewLatest/<int:pid>/',views.viewLatest,name="View-Latest"),
    path('bookingworker/<int:wid>',views.bookingworker,name="workerbooking"),
    path('viewbookedworker/',views.viewbookedworker,name="viewbookdworker"),
    path('paymentworker/<int:pid>',views.paymentworker,name="paymentforworker"),
    path('Contact/<int:coid>',views.Contactworker,name="contactworker"),
    path('balanceworker/<int:pid>',views.balanceworker,name="balanceforworker"),
    

    

    


]