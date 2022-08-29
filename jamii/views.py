from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Volunteer
from .serializer import VolunteerSerializer
from rest_framework import status
# Create your views here.

class Volunteer(APIView):
  def get(self,request,format=None):
    all_volunteer = Volunteer.objects.all()
    serializers= VolunteerSerializer(all_volunteer,many=True)
    return Response(serializers.data)
class Volunteer(APIView):
  def post(self,request,format=None):
    serializers = VolunteerSerializer(data=request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data, status = status.HTTp_400_BAD_REQUEST)
