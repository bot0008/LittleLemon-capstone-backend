from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers

# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.PositiveBigIntegerField()
    
    def __str__(self):
        return f'{self.title} : {str(self.price)}'
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.PositiveBigIntegerField()
    booking_date = models.DateTimeField()
    
    def __str__(self):
        return f"Booking by {self.name} - {self.booking_date}"     
    
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']   