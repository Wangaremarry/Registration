from multiprocessing import context
from os import confstr_names
from pyexpat.errors import messages
from re import template
from venv import create
from django.shortcuts import render
from dateutil.parser import parse


# Create your views here.easy on me adele

import csv, io
from django.contrib.auth.decorators import permission_required

from nuru.models import Users

@permission_required('admin.can_add_log_entry')
def contact_upload(request):
    template="contact_upload.html"
    
    prompt={
        'order':'Order of the CSV should be first_name, last_name,phone_number,child_name,child_date_of_birth,registration_date'
    }
    
    # GET request returns the value of the data with the specified key.

    if request.method== "GET":
        return render(request,template,prompt)
    
    csv_file=request.FILES['file']
    
     # let's check if it is a csv file

    if not csv_file.name.endswith('.csv'):
        messages.error(request,'This is not a csv file')
        
    data_set=csv_file.read().decode('UTF-8')
    
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
  
    io_string=io.StringIO(data_set) 
    next(io_string)
    contact_upload= csv.reader(io_string,delimiter=',', quotechar="|")
    print(contact_upload)
    for full_name,phone_number,child_name,child_date_of_birth, appointment_date,registration_date, *__ in contact_upload:
        dt = parse(child_date_of_birth)
        dts = parse(registration_date)
        created=Users( 
        full_name=full_name,
        child_name=child_name,
        child_date_of_birth=dt,
        registration_date=dts,
        phone_number=phone_number,
        appointment_date = appointment_date

        )
        print(created)
        created.save()    
        
        context={}
        return render(request,template,context)
        
    
    