from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def apiOverview(request):
    apiUrls={
        'AUTHENTICATION' : ' ',
        # account/ password/reset/ [name='rest_password_reset']
        'rest_password_reset        ' : 'user/password/reset/',
        'rest_password_reset_confirm' : 'user/password/reset/confirm/',
        'rest_login                 ' : 'user/login/',
        'rest_logout                ' : 'user/logout/',
        'rest_user_details          ' : 'user/user/',
        'rest_password_change       ' : 'user/password/change/',
        'Registration               ' : 'user/signup/',
        'google_login               ' : 'user/google/',
        
        
        
        'about   ' : 'about/',
        
        'admin   ' : 'admin/'  
    }
    return Response(apiUrls)