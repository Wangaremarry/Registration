from django.db import models

# from django.utils import timezone

# from django.contrib.auth.models import AbstractUser


class Users(models.Model):
    full_name= models.CharField(max_length=20,null=True)
    phone_number= models.CharField(max_length=15,null=True)
    child_name = models.CharField(max_length=30,null=True)
    child_date_of_birth = models.DateField()
    registration_date = models.DateField()
    appointment_date = models.DateField()

class category(models.Model):
    neonatal_information=models.CharField(max_length=250,null=True)
    clinical_information=models.CharField(max_length=250,null=True)
    
class Information(models.Model):
    neonatal_information=models.CharField(max_length=250,null=True)
    clinical_information=models.CharField(max_length=250,null=True)

class Notification(models.Model):
    title=models.CharField(max_length=30,null=True)
    message = models.CharField(max_length=200,null=True)
    date_time = models.DateTimeField(null=True)

class Registration(models.Model):
    first_name= models.CharField(max_length=20,null=True)
    last_name= models.CharField(max_length=20,null=True)
    phone_number=models.CharField(max_length=10, null=True)
    password=models.CharField(max_length=8,null=True)
    password2=models.CharField(max_length=8,null=True)
    


    