from django.urls import path
from Admin import views
app_name='Admin'
urlpatterns = [
     
     
    path('district/',views.district,name="District"),
    path('deletedist/<int:uid>',views.districtdelete,name="dltuser"),
    path('upadtedist/<int:uid>',views.districtupdate,name="upddist"),
    path('Place/',views.place,name="place"),
    path('deleteplace/<int:uid>',views.Placedelete,name="dltplace"),
    path('updateplace/<int:uid>',views.Placeupdate,name="updplace"),
    path('Workcategory/',views.workcategory,name="work"),
    path('deleteworkcategory/<int:uid>',views.workcategorydelete,name="dltworkcategory"),
    path('updateworkcategory/<int:uid>',views.workcategoryupdate,name="updateworkcategory"),
    path('landfactors/',views.landfactors,name="Land"),
    path('deletelandfactors/<int:uid>',views.landfactorsdelete,name="dltlandfactors"),
    path('updatelandfactors/<int:uid>',views.landfactorsupdate,name="updatelandfactors"),
    path('complaint/',views.complaintype,name='complaint'),
    path('deletecomplaint/<int:uid>',views.complaintdelete,name="dltlandcomplaints"),
    path('updatecomplaint/<int:uid>',views.complaintsupdate,name="updatecomplaints"),
    path('condract/',views.condractservice,name='Condract'),
    path('deletecontract/<int:uid>',views.contactservicedelete,name="dltcontractservice"),
    path('updatecontract/<int:uid>',views.contractserviceupdate,name="updatecontractservice"),
    path('newuser/',views.viewuserdetails,name="viewuser"),
    path('newconstructor/',views.viewnewconstuctor,name="viewconstructor"),
    path('acceptconstructor/<int:aid>/',views.constructoraccept,name="accept"),
    path('rejectconstructor/<int:did>/',views.constructorreject,name="reject"),
    path('adminhome/',views.Adminhome,name="Admimnhome"),
    path('viewworker/',views.viewworker,name="Viewwrkr"),
    path('viewwlandlord/',views.viewlandlord,name="viewlandlord"),
    path('acceptlandlord/<int:lid>/',views.accept,name="acceptlandlord"),
    path('rejectlandlord/<int:rid>/',views.reject,name="rejectlandlord"),
    path('viewallfeedbacks/',views.allfeedbacks,name="ViewAllFeedbacks"),
    path('home/',views.indexpage,name="home-admin"),
    path('usercomplaint/',views.usercomp,name="user-complaint"),
    path('usercompreplay/<int:cid>/',views.Replay,name="Replay"),
    path('workercomplaint/',views.workercomp,name="worker-complaint"),
    path('workercompreplay/<int:wid>/',views.workerReplay,name="workerReplay"),
    path('constructorcomplaint/',views.conscomp,name="cons-complaint"),
    path('conscompreplay/<int:wid>/',views.consReplay,name="consReplay"),
    path('landlordcomplaint/',views.landcomp,name="land-complaint"),
    path('landcompreplay/<int:wid>/',views.landReplay,name="landReplay"),
    
    
    
]