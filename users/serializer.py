from rest_framework import serializers
from .models import userDetails
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields='__all__'
        
class userdetailSerializer(serializers.ModelSerializer):
    # user = UserSerializer(read_only=True, source='user.user')
    user = UserSerializer(required=True)

    class Meta:
        model = userDetails
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        profile, created = userDetails.objects.update_or_create(user=user,
                            subject_major=validated_data.pop('subject_major'))
        return profile
    
    # class Meta:
    #     model=userDetails
    #     user = User.pk
    #     optional_fields = ['avatar']
    #     exclude = ('user',)
    #     # fields='__all__'