from .models import Volunteer,Blood,Contact
from .serializer import VolunteerSerializer,ContactSerializer,BloodSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
@api_view(['GET','POST'])
def volunteer_list(request,format=None):
    if request.method == 'GET':
      volunteers = Volunteer.objects.all()
      serializers= VolunteerSerializer(volunteers,many=True)
      return Response(serializers.data)
    elif request.method == 'POST':
      serializers = VolunteerSerializer(data=request.data)
      if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status = status.HTTP_201_CREATED)
      return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['PUT','DELETE','GET'])
def volunteer_detail(request,pk,format=None):
  try:
    volunteer = Volunteer.objects.get(pk=pk)
  except Volunteer.DoesNotExist:
    return Response(status=start.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializers = VolunteerSerializer(Volunteer)
    return Response(serializers.data)
  elif request.method == 'PUT':
    serializers = VolunteerSerializer(volunteer, data=request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data)
    return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def contact_list(request,format=None):
    if request.method == 'GET':
      contacts = Contact.objects.all()
      serializers= ContactSerializer(contacts,many=True)
      return Response(serializers.data)
    elif request.method == 'POST':
      serializers = ContactSerializer(data=request.data)
      if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status = status.HTTP_201_CREATED)
      return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['PUT','DELETE','GET'])
def contact_detail(request,pk,format=None):
  try:
    contact = Contact.objects.get(pk=pk)
  except Contact.DoesNotExist:
    return Response(status=start.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializers = ContactSerializer(Contact)
    return Response(serializers.data)
  elif request.method == 'PUT':
    serializers = ContactSerializer(contact, data=request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data)
    return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','POST'])
def blood_list(request,format=None):
    if request.method == 'GET':
      bloods = Blood.objects.all()
      serializers= BloodSerializer(bloods,many=True)
      return Response(serializers.data)
    elif request.method == 'POST':
      serializers = BloodSerializer(data=request.data)
      if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status = status.HTTP_201_CREATED)
      return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['PUT','DELETE','GET'])
def blood_detail(request,pk,format=None):
  try:
    blood = Blood.objects.get(pk=pk)
  except Blood.DoesNotExist:
    return Response(status=start.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializers = BloodSerializer(Contact)
    return Response(serializers.data)
  elif request.method == 'PUT':
    serializers = BloodSerializer(blood, data=request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data)
    return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


