from rest_framework import serializers
from .models import Business_idaea, Comment, Offers


class business_idaeaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Business_idaea
        fields = '__all__'


class commentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'

class offersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Offers
        fields = '__all__'