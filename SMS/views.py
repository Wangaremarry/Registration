from django.shortcuts import render
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
@csrf_exempt
def registration(request):
    if request.method == 'POST':
        session_id = request.POST.get('sessionId')
        short_code = request.POST.get('shortcode')
        phone_number = request.POST.get('phoneNumber')
        text = request.POST.get('text')
        response=""
        if text == "":
            response = "CON Welcome to nuruCare \n"
            response += "Press 1 to opt-out \n"

    return HttpResponse({"NuruCare": "this method requires a POST "})


