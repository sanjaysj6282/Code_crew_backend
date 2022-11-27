from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView

from .serializer import userdetailSerializer
from .models import userDetails
from rest_framework import status
from rest_framework.response import Response
# api_view is a must when using Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

class GoogleLogin(SocialLoginView): # if you want to use Authorization Code Grant, use this
    adapter_class = GoogleOAuth2Adapter
    callback_url = "http://127.0.0.1:8000/user/google"
    client_class = OAuth2Client
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createProfile(request):
    if request.method=='POST':
        serialized_data=userdetailSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        serialized_data=userdetailSerializer()
    return Response({'error: 0'})    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def details(request, userName):
    user_details=userDetails.objects.get(id=userName)
    serialized_data=userdetailSerializer(user_details)
    return Response(serialized_data.data)