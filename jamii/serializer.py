from rest_framework import serializers
from .models import Volunteer,Contact,Blood
class VolunteerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Volunteer
    fields = ('full_names','email','phone_number','location')

class ContactSerializer(serializers.ModelSerializer):
  class Meta:
    model = Contact
    fields = ('username','email','subject','message')

class BloodSerializer(serializers.ModelSerializer):
  class Meta:
    model = Blood
    fields = ('location','hospital','blood_Type','date')