from django.urls import path
from Admin.views import viewuserdetails
from Guest import views
app_name='Guest'
urlpatterns = [
path('Newuser/',views.newuser,name="newuserreg"),
path('loadplace/',views.placeload,name="load_place"),
path('newcondractor/',views.newcondractor,name="newcondractorreg"),
path('newworker/',views.newworker,name="newworkerreg"),
path('login/',views.Login,name="Login"),
path('Newlandlord/',views.Landlord,name="newlandlord"),
path('register/',views.register,name="registerpage"),
path('about/',views.about,name="About"),
path('contact/',views.contact,name="Contact"),
path('Thank/',views.Thankyou,name="Thankyou1"),
path('Thanks/',views.Thanksverify,name="Thankss"),



]