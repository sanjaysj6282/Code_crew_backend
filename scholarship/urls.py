from django.urls import path, include
from . import views

app_name = 'scholarship'

urlpatterns = [  
    path('list/', views.listDetails,name='list events'),
    path('add/', views.create, name='create_profile'),
    path('details/<currId>', views.details, name='user_details'),
    path('update/<currId>', views.updateDetails, name='update_details'),
    path('delete/<currId>', views.deleteDetails, name='delete_details')
]