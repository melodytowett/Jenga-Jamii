from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
import .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly
from django.core.exceptions import ObjectDoesNotExist



# Create your views here.
class StudentList(APIView):
      permission_classes = (IsAdminOrReadOnly,)
    def get(self,request,format=None):
        all_students =Student.objects.all()
        serializers =StudentSerializer(all_students, many=True)
        return Response(serializers.data)

     def post(self, request, format=None):
        serializers =StudentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)    


class StudentDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_student(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.ObjectDoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        student = self.get_student(pk)
        serializers = StudentSerializer(student)
        return Response(serializers.data)


     def put(self, request, pk, format=None):
        student = self.get_student(pk)
        serializers = StudentSerializer(student, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)  

     def delete(self, request, pk, format=None):
        student = self.get_student(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)          