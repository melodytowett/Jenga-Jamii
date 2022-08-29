from rest_framework import serializers
from .models import Volunteer
class VolunteerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Volunteer
    fields = ('full_names','email','phone_number','location')

class ContactSerializer(serializers.ModelSerializer):
  class Meta:
    model = Contact
    fields = ('username','email','subject','message')