from django.urls import path, include
from . import views

app_name = 'events'

urlpatterns = [    
    path('list/', views.listDetails,name='list events'),
    
    path('add/', views.createProfile, name='create_profile'),
    path('details/<currId>', views.details, name='user_details'),
    path('updateDetails/<currId>', views.updateDetails, name='update_details'),
    path('deleteDetails/<currId>', views.deleteDetails, name='delete_details')
]