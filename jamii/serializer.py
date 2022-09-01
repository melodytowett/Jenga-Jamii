from rest_framework import serializers
from .models import Volunteer,Contact,Blood,DonateTo,Donations
from django.contrib.auth.models import User
class VolunteerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Volunteer
    fields = ('id','full_names','email','phone_number','location')

class ContactSerializer(serializers.ModelSerializer):
  class Meta:
    model = Contact
    fields = ('id','username','email','subject','message')

class BloodSerializer(serializers.ModelSerializer):
  class Meta:
    model = Blood
    fields = ('id','location','hospital','blood_Type','date')

class DonateToSerializer(serializers.ModelSerializer):
  class Meta:
    model = DonateTo
    fields = ('id','schools','orphanages','society','hospitals','prisons','refugees')
class DonationsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Donations
    fields = ('id','donate_to','donation_type','upload_image')