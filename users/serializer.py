from rest_framework import serializers
from .models import userDetails
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields='__all__'
        # field=('pk', )  
            
class userdetailSerializer(serializers.ModelSerializer):
    # user = User.objects.get(pk=2)
    user = serializers.PrimaryKeyRelatedField(
        read_only=True, default=serializers.CurrentUserDefault()
    )
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # id=serializers.HiddenField(default=serializers.CurrentUserDefault())
    # user=serializers
    # user = User.objects.all().get('pk')
    # user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=False)
    class Meta:
        model = userDetails
        # user = UserSerializer(required=True)
        fields='__all__'
        # fields = ('user', 'phone_no', 'programme', 'course', 'gender', 'category', 'income',)

    # def create(self, validated_data):
    #     user_data = validated_data.pop('user')
    #     user = UserSerializer.create(UserSerializer(), validated_data=user_data)
    #     profile, created = userDetails.objects.update_or_create(user=user,
    #                         subject_major=validated_data.pop('subject_major'))
    #     return profile
    
    # class Meta:
    #     model=userDetails
    #     user = User.pk
    #     optional_fields = ['avatar']
    #     exclude = ('user',)
    #     # fields='__all__'