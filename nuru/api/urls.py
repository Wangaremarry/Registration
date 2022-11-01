from django.urls import path

from nuru.api.views import(
    registration_view,
)

urlspatterns = [
    path('register', registration_view, name='register'),
]
