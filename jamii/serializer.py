from rest_framework import serializers
from models import Student

class StudentSerializer(serializers.ModelSerializers):
    class Meta:
        model= Student
        fields =('id','first_name','last_name','date_of_birth','grade','phone','email')
