from rest_framework import serializers
from .models import userDetails
from django.contrib.auth.models import User

from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer

# Added custom serializer for adding first name
# https://stackoverflow.com/questions/62291394/django-rest-auth-dj-rest-auth-custom-user-registration
class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField()

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()
        return {
            'first_name': self.validated_data.get('first_name', ''),
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', '')
        }

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields='__all__'
#         # field=('pk', )  
            
class userdetailSerializer(serializers.ModelSerializer):
    # user = User.objects.get(pk=2)
    # user = serializers.PrimaryKeyRelatedField(
    #     read_only=True, default=serializers.CurrentUserDefault()
    # )
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # user=serializers
    # user = User.objects.all().get('pk')
    # user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=False)
    # user = UserSerializer(required=False)
    # user = serializers.CurrentUserDefault()
    # user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = userDetails
        # user = UserSerializer(required=True)
        fields='__all__'
        # fields = ('user', 'phone_no', 'programme', 'course', 'gender', 'category', 'income',)

    # def create(self, validated_data):
    #     user_data = validated_data.pop('user')
    #     user = UserSerializer.create(UserSerializer(), validated_data=user_data)
    #     profile, created = userDetails.objects.update_or_create(user=user)
    #     return profile
    
    # class Meta:
    #     model=userDetails
    #     user = User.pk
    #     optional_fields = ['avatar']
    #     exclude = ('user',)
    #     # fields='__all__'