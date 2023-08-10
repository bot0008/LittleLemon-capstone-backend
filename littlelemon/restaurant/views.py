from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Menu
from .serializers import MenuSerializer
from .models import Booking
from .serializers import BookingSerializer
from rest_framework import viewsets, permissions

# Create your views here.
def sayHello(request):
    return HttpResponse('Hello World')

def index(request):
    return render(request, 'index.html', {}) 

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated] 
        
    
    
        