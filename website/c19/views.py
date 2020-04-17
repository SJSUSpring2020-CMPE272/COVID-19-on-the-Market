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
        server = "https://iam.bluemix.net/oidc/token"
        IBM_cloud_IAM_uid = "bx"
        IBM_cloud_IAM_pw = "bx"
        auth = (IBM_cloud_IAM_uid, IBM_cloud_IAM_pw)
        response = requests.post(server, headers=headers, data=data, auth=auth)
        response_json = json.loads(response.text)
        access_token = response_json['access_token']
        return access_token

def get_ml_instance_id():
    return "54369f40-6048-478f-ba00-5c1653af7aa6"

def construct_payload(inputArray):
    payload = {"input_data": 
                [
                    {"fields": ["key_0", 
                                "DGS10 [%]", 
                                "T10YIE[%]",
                                "Confirmed COVID-19 cases", 
                                "Recovered COVID-19 cases", 
                                "Deaths due to COVID-19 ", 
                                "Initial unemployment claims (Seasonally adjusted)", 
                                "Weekly U.S. All Grades All Formulations Retail Gasoline Prices (Dollars per Gallon)", 
                                "Weekly U.S. No 2 Diesel Retail Prices  (Dollars per Gallon)"
                                ], 
                    "values": inputArray}
                ]
            }
    return payload



def get_server_url():
    url = 'https://us-south.ml.cloud.ibm.com/v4/deployments/3861dfa6-8e65-48f2-b7a3-9bef448a3ea2/predictions'
    return url

def construct_header(iam_token, ml_instance_id):
    header = {'Content-Type': 'application/json', 
              'Authorization': 'Bearer ' + iam_token, 
              'ML-Instance-ID': ml_instance_id}
    return header

def getPrediction(input_payload):
    #ml_instance_id  = get_ml_instance_id()
    #iam_token = generate_iam_token()
    #print("iam_token = ", iam_token)
    #header = construct_header(iam_token, ml_instance_id)
    #payload = input_payload
    #url = get_server_url()

    #response = requests.post(url, json=payload, headers=header)
    #context = json.loads(response.text)
    #print("context = ", context)
    context = {}
    return context

        
def receive(request):
        if (request.method == 'POST'):
            print("In Receive: got post request")
            form = FieldsForm(request.POST)
            context = {}
        if form.is_valid():
            key = form.cleaned_data['key']
            dgs = form.cleaned_data['dgs']
            t10 = form.cleaned_data['t10']
            confirmed_cases = form.cleaned_data['confirmed_cases']
            recovered_cases = form.cleaned_data['recovered_cases']
            deaths = form.cleaned_data['deaths']
            unemployment = form.cleaned_data['unemployment']
            gas_prices = form.cleaned_data['gas_prices']
            diesel_prices = form.cleaned_data['diesel_prices']

            inputArray = [key, dgs, t10, confirmed_cases, recovered_cases, deaths, unemployment, gas_prices, diesel_prices]
            payload = construct_payload(inputArray)
            ML_output = getPrediction(payload)

            context = {"key": key,
                       "dgs": dgs,
                       "t10" : t10,
                       "confirmed_cases" : confirmed_cases,
                       "recovered_cases": recovered_cases,
                       "deaths": deaths,  
                       "unemployment": unemployment,
                       "gas_prices": gas_prices,
                       "diesel_prices": diesel_prices,
                        #"predictions": ML_output['predictions']
                       }
        template = loader.get_template('c19/form_entered.html')
        return HttpResponse(template.render(context, request))

def index(request):
    form = FieldsForm()
    context = {'form': form}
    template = loader.get_template('c19/index.html')
    return HttpResponse(template.render(context, request))

   

    
    

    

    