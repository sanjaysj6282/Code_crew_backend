from django.urls import path, include
from ..events import views_lecture

app_name = 'scholarship'

urlpatterns = [  
    path('lecture/list/', views_lecture.listDetails,name='list events'),
    path('lecture/add/', views_lecture.create, name='create_profile'),
    path('lecture/details/<currId>', views_lecture.details, name='user_details'),
    path('lecture/update/<currId>', views_lecture.updateDetails, name='update_details'),
    path('lecture/delete/<currId>', views_lecture.deleteDetails, name='delete_details')
]