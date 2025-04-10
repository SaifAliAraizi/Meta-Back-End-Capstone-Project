from rest_framework import viewsets, generics
from django.http import HttpResponse
from .models import Menu, Booking
from .serializers import menuSerializer, bookingSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here. 
def index(request):
    return HttpResponse("Welcome to the LittleLemon restaurant API!")
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()  # Retrieve all menu items
    serializer_class = menuSerializer  # Use MenuItemSerializer for formatting the data

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()  # Retrieve the specific menu item
    serializer_class = menuSerializer  # Use the same serializer for single item
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()  # Get all booking objects
    serializer_class = bookingSerializer  # Use the serializer to format the data
    permission_classes = [IsAuthenticated]