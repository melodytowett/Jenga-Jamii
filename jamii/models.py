from django.db import models
from location_field.models.plain import PlainLocationField
# Create your models here.
class Volunteer(models.Model):
  full_names = models.CharField(max_length=200)
  email = models.EmailField(max_length=200)
  phone_number = models.CharField(max_length = 12)
  location = PlainLocationField(based_fields=['city'], zoom=7)
 
  
