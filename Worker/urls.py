from django.urls import path
from Worker import views
app_name='Worker'
urlpatterns = [
    path('ViewProfile/',views.workerdetails,name="View-workerProfile"),
    path('updateworker/<int:wid>/',views.updateworker,name="updateworker"),
    path('changepassword/<int:wid>/',views.changepassword,name="changepassword"),
    path('Addwork/',views.workpofile,name="Addwork"),
    path('Latestwork/<int:wid>',views.Latestwork,name="latestwork"),
    path('viewworkerbooking/',views.viewworkerbook,name="viewworkerbook"),
    path('acceptconstbooking/<int:waid>/',views.acceptworkerbooking,name="accept"),
    path('rejectconstbooking/<int:wdid>/',views.rejectworkerbooking,name="reject"),
    path('Wrkcmplt/<int:wcoid>',views.workcomplete,name="workcmplt"),
    path('index/',views.indexpage,name="index"),
    path('workercomplaints/',views.newcomplaint,name="workerComplaints"),
    path('workerfeedback/',views.workerfeedback,name="workerFeedback"),
    path('deletworker/<int:workerid>',views.dlt,name="dltworker"),
   
]
    
    

