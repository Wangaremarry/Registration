# from tkinter.ttk import Style
from rest_framework import serializers
from nuru.models import Registration

class RegistrationSerialzer(serializers.ModelSerializer):
 password2= serializers.CharField(write_only=True)

class Meta:
    model=Registration
    field=['first_name', 'last_name','phone_number','password','password2']
    extra_kwargs={
        'password':{'write_only':True}
    }
def save(self):
    registration=Registration(
        first_name=self.validate_data['first_name'],
        last_name=self.validate_data['last_name']
    )
    password=self.validate_data['password']
    password2=self.validate_data['password2']
    
    if password!=password2:
        raise serializers.ValidationError({'password':'Password must match'})
    
    registration.set_password(password)
    registration.save()
    return registration
    