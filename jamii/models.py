from django.db import models
from location_field.models.plain import PlainLocationField
# Create your models here.

class DonateTo(models.Model):
  schools = models.CharField(max_length=200)
  orphanages= models.CharField(max_length=200)
  society = models.CharField(max_length=200)
  hospitals = models.CharField(max_length=200)
  prison = models.CharField(max_length=200)
  refugees = models.CharField(max_length=200)

class Donations(models.Model):
  donate_to = models.ForeignKey(DonateTo,on_delete=models.CASCADE)
  donation_type = models.CharField(max_length=200)
  upload_image = models.ImageField(upload_to = 'image/',blank = True)

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
  hospital = models.CharField(max_length=100)
  blood_Type = models.CharField(max_length = 3)
  date_time = models.DateTimeField()

  
  
