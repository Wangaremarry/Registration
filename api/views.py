from rest_framework import viewsets
from .serializers import InformationSerializer,NotificationSerializer, UsersSerializer
from nuru import models



class UsersViewSet(viewsets.ModelViewSet):
    queryset=models.Users.objects.all()
    serializer_class = UsersSerializer

class InformationViewSet(viewsets.ModelViewSet):
    queryset=models.Information.objects.all()
    serializer_class = InformationSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    queryset=models.Notification.objects.all()
    serializer_class = NotificationSerializer




