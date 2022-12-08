from django.urls import path, include
from . import views_workshop, views_lecture

app_name = 'events'

urlpatterns = [  
                 
    path('workshop/list/', views_workshop.list,name='list worshop'),
    path('workshop/add/', views_workshop.create, name='create_profile'),
    path('workshop/details/<currId>', views_workshop.details, name='user_details'),
    path('workshop/update/<currId>', views_workshop.update, name='update_details'),
    path('workshop/delete/<currId>', views_workshop.delete, name='delete_details'),
    
    path('lecture/list/', views_lecture.list,name='list events'),
    path('lecture/add/', views_lecture.create, name='create_profile'),
    path('lecture/details/<currId>', views_lecture.details, name='user_details'),
    path('lecture/update/<currId>', views_lecture.update, name='update_details'),
    path('lecture/delete/<currId>', views_lecture.delete, name='delete_details')
]