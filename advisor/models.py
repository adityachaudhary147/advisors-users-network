from django.db import models

# Create your models here.
class Advisor(models.Model):
    name=models.CharField(max_length=255)
    photo_url=models.CharField(max_length=255)

class Booking(models.Model):
    booking_time=models.DateTimeField()
    advisor=models.ForeignKey(Advisor,on_delete=models.CASCADE)

