from rest_framework import serializers
from .models import Advisor,Booking

class AdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Advisor
        fields="__all__"


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
    
