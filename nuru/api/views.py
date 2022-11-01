from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from nuru.api.serializers import RegistrationSerialzer

@api_view(['POST',])
def registration_views(request):
    if request.method=='POST':
        serializer=RegistrationSerialzer(data=request.data)
        data={}
        if serializer.is_valid():
            nuru=serializer.save()
            data['response']='Successfully reistered a new user.'
            data['first_name']= nuru.first_name
            data['last_name']= nuru.last_name
            data['pssword']= nuru.password
        else:
            data=serializer.errors
            return Response(data)