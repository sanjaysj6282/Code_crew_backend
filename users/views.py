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
from django.contrib.auth.models import User
from rest_framework import serializers
from django.shortcuts import get_object_or_404
from . import models


# if you want to use Authorization Code Grant, use this
class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = "http://127.0.0.1:8000/user/google"
    client_class = OAuth2Client



@api_view(['POST'])
@permission_classes([IsAuthenticated])
# error solved
# https://stackoverflow.com/questions/27934822/get-current-user-in-model-serializer
def createProfile(request):
    # curr_user = None
    # request = self.context.get("request")
    # if request and hasattr(request, "user"):
    #     curr_user = request.user
    curr_user=request.user
    
    # data=request.data
    # curr_user=User.objects.get(id=data['id'])
    serializer = userdetailSerializer(data=request.data, context={'request': request})
    if serializer.is_valid(raise_exception=ValueError):
        serializer.save(
            user_id=curr_user.id
            # user=curr_user
            # user=User.
        )
        # serializer.create(validated_data=request.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


# def sample_view(request):
#     current_user = request.user
#     return HttpResponse(current_user.id) 

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def details(request):
    # curr_user=request.user
    # user_details = userDetails.objects.get(id=curr_user.id)
    # curr_user=get_object_or_404(userDetails, user__user__username=username)
    # user_details = User.objects.all().select_related('userDetails')
    curr_user=request.user
    user_details=userDetails.objects.get(user=curr_user)
    serialized_data = userdetailSerializer(user_details, context={'request': request})
    return Response(serialized_data.data)
