from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Menu
from .models import Booking
from rest_framework.authtoken.models import Token

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'