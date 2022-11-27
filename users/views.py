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
from django.views.decorators.csrf import csrf_exempt

# if you want to use Authorization Code Grant, use this
class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = "http://127.0.0.1:8000/user/google"
    client_class = OAuth2Client


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createProfile(request):
    curr_user=request.user
    serializer = userdetailSerializer(data=request.data)
    if serializer.is_valid(raise_exception=ValueError):
        serializer.save(
            id=curr_user.id
        )
        # serializer.create(validated_data=request.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


# def sample_view(request):
#     current_user = request.user
#     return HttpResponse(current_user.id) 

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def details(request, userName):
    user_details = userDetails.objects.get(id=userName)
    serialized_data = userdetailSerializer(user_details)
    return Response(serialized_data.data)
