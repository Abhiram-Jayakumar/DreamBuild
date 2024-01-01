from django.urls import path
from Landlord import views
app_name='Landlord'
urlpatterns = [
path('index/',views.indexpage,name="index"),
path('ViewProfile/',views.Landlorddetails,name="View-Profile"),
path('updateLandlord/<int:cid>/',views.updateLandlrd,name="Update"),
path('changepassword/<int:cid>/',views.changepassword,name="changepassword"),
path('manageland/',views.managelandsoflord,name="manageland"),
path('Landfacilities/<int:cid>/',views.landfacilities,name="landfacililities"),
path('Landgallery/<int:cid>/',views.landssgallery,name='landgalry'),
path('deletelndgallery/<int:did>/',views.dltlndgallery,name="dltlndgallery"),
path('viewlandbooking/',views.viewlandbook,name="viewlandbook"),
path('acceptlandbooking/<int:aid>/',views.acceptlandbooking,name="accept"),
path('rejectlandbooking/<int:did>/',views.landbookingreject,name="reject"),
path('landfeedback/',views.Landfeedback,name="landFeedback"),
path('landcomplaints/',views.Landcomplaint,name="landComplaints"),
path('deletelandlord/<int:landlordid>',views.dlt,name="dltlandlord"),










]