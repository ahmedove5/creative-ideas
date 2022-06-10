from rest_framework import serializers
from .models import Profile ,Comment

class profileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'


class commentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'