from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 
import requests
import json 
import urllib3
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import FieldsForm

def generate_iam_token():
        headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Accept': 'application/json'}
        data = {'grant_type':'urn:ibm:params:oauth:grant-type:apikey', 'apikey':'zchGXyAjaMtNldcCjII5EuLdc_xFxkJhagKIc32FHxV_'}
        server =  "https://iam.cloud.ibm.com/identity/token" 
        response = requests.post(server, headers=headers, data=data)
        response_json = json.loads(response.text)
        access_token = response_json['access_token']
        print(access_token)
        return access_token

def get_ml_instance_id():
    return "54369f40-6048-478f-ba00-5c1653af7aa6"

def get_sample_payload():
    payload= {
        "input_data": [
            {"fields": 
                ["No", 
                "X1 transaction date", 
                "X2 house age", 
                "X3 distance to the nearest MRT station", 
                "X4 number of convenience stores", 
                "X5 latitude", 
                "X6 longitude"], 
			    "values": [
                    [1, 2010.917, 2, 84, 10, 24.98, 121.54]
                ]
            }
        ]
    }
    return payload

def get_server_url():
    url = 'https://us-south.ml.cloud.ibm.com/v4/deployments/9300bf9d-85c7-4edd-9cba-22f65a748485/predictions' 
    return url
        
def receive(request):
        if (request.method == 'POST'):
            print("In Receive: got post request")
            form = FieldsForm(request.POST)
            context = {}
        if form.is_valid():
            transaction_date = form.cleaned_data['transaction_date']
            house_age = form.cleaned_data['house_age']
            distance_to_station = form.cleaned_data['distance_to_station']
            number_of_stores = form.cleaned_data['number_of_stores']
            latitude = form.cleaned_data['latitude']
            longitude = form.cleaned_data['longitude']
            context = {"transaction_date":transaction_date,
                       "house_age": house_age,
                       "distance_to_station" : distance_to_station,
                       "number_of_stores" : number_of_stores,
                       "latitude": latitude,
                       "longituge": longitude,}
        template = loader.get_template('c19/form_entered.html')
        return HttpResponse(template.render(context, request))

def index(request):
     
    #ml_instance_id  = get_ml_instance_id()
    #iam_token = generate_iam_token()
    #header = {'Content-Type': 'application/json', 
    #          'Authorization': 'Bearer ' + iam_token, 
    #          'ML-Instance-ID': ml_instance_id}
    #payload = get_sample_payload()
    #url = get_server_url()

    #response = requests.post(url, json=payload, headers=header)
    #context = json.loads(response.text)
    #print("context = ", context)

    
    form = FieldsForm()
    context = {'form': form}
    template = loader.get_template('c19/index.html')
    return HttpResponse(template.render(context, request))

   

    
    

    

    