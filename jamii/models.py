from django.db import models
from phone_field import PhoneField

# Create your models here.

class Student(models.Model):
    first_name =models.CharField(max_length=40)
    last_name =models.CharField(max_length=40)
    date_of_birth =models.DateField()
    grade =models.CharField(max_length=5)
    phone =models.PhoneField(blank=True, help_text='Contact phone number')
    email =models. models.EmailField(max_length = 254)

    def __str__(self):
        return self.first_name



