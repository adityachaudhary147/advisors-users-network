from django.shortcuts import render
from rest_framework.generics import ListAPIView
# Create your views here.
from .serializers import AdvisorSerializer,BookingSerializer
from .models import Advisor,Booking
from rest_framework.views import APIView

from rest_framework.response import Response    
from users.models import User




class AdvisorList(ListAPIView):
    serializer_class = AdvisorSerializer

    def get_queryset(self, *args, **kwargs):
        """
        This view should return a list of all the advisors
        for any user
        """
        return Advisor.objects.all()


class AdvisorView(APIView):
    def post(self, request,*args, **kwargs ):
        serializer = AdvisorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class BookingList(ListAPIView):

    serializer_class = BookingSerializer

    def get_queryset(self, *args, **kwargs):
        """
        This view should return a list of all the advisors
        for any user
        """

        return Booking.objects.all()

class BookingView(APIView):
    def post(self, request,*args, **kwargs):
        booking = Booking(booking_time=request.data['booking_time'], advisor=Advisor.objects.get(id=kwargs['gk']))
        booking.save()
        return Response({"message":"Success"})
