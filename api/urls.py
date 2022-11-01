from django.urls import include ,path
from rest_framework import routers
from .views import InformationViewSet,NotificationViewSet, UsersViewSet



router =routers.DefaultRouter()
router.register(r'Users',UsersViewSet),
router.register(r'Information',InformationViewSet)
router.register(r'Notification',NotificationViewSet)



urlpatterns=[
    path('',include(router.urls)),

]

