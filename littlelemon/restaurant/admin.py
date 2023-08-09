from django.contrib import admin
from .models import Menu, Booking

# Register your models here.

class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'inventory')

class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'no_of_guests', 'booking_date')    