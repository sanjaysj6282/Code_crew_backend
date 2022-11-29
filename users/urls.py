from django.urls import path, include
from dj_rest_auth.registration.views import VerifyEmailView
from django.views.decorators.csrf import csrf_exempt
from . import views

app_name = 'users'

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('registration/', include('dj_rest_auth.registration.urls')),
    path('google/', views.GoogleLogin.as_view(), name='google_login'),
    
    
    path('list/', views.listDetails,name='list users'),
    
    path('add/', views.createProfile, name='create_profile'),
    path('details/', views.details, name='user_details'),
    path('updateDetails/', views.updateDetails, name='update_details'),
    path('deleteDetails/', views.deleteDetails, name='delete_details')
]