from dataclasses import field, fields
from operator import mod
from pyexpat import model
from rest_framework import serializers
from nuru.models import Information,  Notification, Users
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password




class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields =('full_name','phone_number' ,'child_name','child_date_of_birth','registration_date','appointment_date')

class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields =('neonatal_information','clinical_information')


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Notification
        fields=('title','message','date_time')




