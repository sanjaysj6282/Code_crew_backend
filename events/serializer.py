from rest_framework import serializers
from .models import Workshop, Exam, Lecture

class workshopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workshop
        fields='__all__'