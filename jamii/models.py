from django.db import models
from location_field.models.plain import PlainLocationField
# Create your models here.
class Volunteer(models.Model):
  full_names = models.CharField(max_length=200)
  email = models.EmailField(max_length=200)
  phone_number = models.CharField(max_length = 12)
  location = PlainLocationField(based_fields=['city'], zoom=7)
 
class Contact(models.Model):
  username = models.CharField(max_length=200)
  email = models.EmailField(max_length=200)
  subject = models.CharField(max_length= 300)
  message = models.CharField(max_length = 500)

class Blood(models.Model):
  location = PlainLocationField(based_fields = ['city'],zoom=7)
  Hospital = models.CharField(max_length=100)
  Blood_Type = models.CharField(max_length = 3)
  date_time = models.DateTimeField()

  
  
