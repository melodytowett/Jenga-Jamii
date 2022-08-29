from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Volunteer
from .serializer import VolunteerSerializer
# Create your views here.

class Volunteer(APIView):
  def get(self,request,format=None):
    all_volunteer = Volunteer.objects.all()
    serializers= VolunteerSerializer(all_volunteer,many=True)
    return Response(serializers.data)
