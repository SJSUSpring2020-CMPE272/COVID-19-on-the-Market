from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 
import requests
import json 
import urllib3
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os 
from decimal import Decimal


from .forms import FieldsForm

def run_script():
    initialValue = np.array(["2019-01-02", 2.66, 1.7, 0, 0, 0, 220000, 2.329, 3.013])
    singleRow = pd.DataFrame([initialValue],
                      columns=["date", 'DGS10[\%]', "T10YIE[\%]", "Confirmed Cases", "Recovered Cases",
                                "Deaths", "Unemployment Claims", "Weekly Gas Avg", "Weekly Diesal Avg"])
    addedValue = singleRow
    for n in range(0,500):
        singleRow['Unemployment Claims'] = int(singleRow['Unemployment Claims'].values[0]) + 100
        addedValue = pd.concat([addedValue, singleRow])
    values = addedValue.values.tolist() 
    input_array = [[2.66, 1.7, 1000, 200, 50, 220100.0, 2.329, 3.013],
		     						 [0.73,0.73,4632,17,85,3307000,2.343,2.733],
		    							  [0.76,1,959,8,28,282000,2.343,2.733],
		   									   [0.92,0.75,19100,147,244,3307000,2.217,2.659],
		      										[0.72,0.94,121478,1072,2026,6648000,2.103,2.586]]


    #payload = construct_payload(input_array)
    #predictions = getPrediction(payload)
    #print("predictions = " + str(predictions))
    
    predictions = {'predictions': [{'fields': ['prediction'], 'values': [[2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2536.1139892578126], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2536.1139892578126], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2536.1139892578126], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2551.5869873046877], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2551.5869873046877], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2551.5869873046877], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2551.5869873046877], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2551.5869873046877],]}]}

    dataPoints = predictions["predictions"][0]["values"]
    y = np.linspace(1, len(dataPoints), len(dataPoints))
    
    figure = plt.figure()
    new_plot = figure.add_subplot(111)
    new_plot.plot(y, dataPoints, color="#ffffff", linewidth=1, markerfacecolor="#ffffff")

    #plt.plot(y, dataPoints, color="#ffffff", linewidth=3, markerfacecolor="#ffffff")
    new_plot.spines['bottom'].set_color('#ffffff')
    new_plot.spines['top'].set_color('#ffffff') 
    new_plot.spines['right'].set_color('#ffffff')
    new_plot.spines['left'].set_color('#ffffff')

    for axis in ['bottom','left']:
        new_plot.spines[axis].set_linewidth(3)

    for axis in ['top','right']:
        new_plot.spines[axis].set_linewidth(0)


    new_plot.tick_params(axis='x', colors='white')
    new_plot.tick_params(axis='y', colors='white')
    
    new_plot.set_xlabel('X-axis')
    new_plot.set_ylabel('Y-axis')

    new_plot.yaxis.label.set_color('white')
    new_plot.xaxis.label.set_color('white') 

    #my_path = os.path.abspath(__file__)
    #if os.path.isfile('c19/static/images/test_graph.png'):
    #    os.remove('c19/static/images/test_graph.png')
    #plt.savefig('c19/static/images/test_graph.png', transparent=True)
    plt.savefig('c19/static/images/test_graph.png', transparent=True)


def generate_iam_token():
        headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Accept': 'application/json'}
        # apikey = 'zchGXyAjaMtNldcCjII5EuLdc_xFxkJhagKIc32FHxV_' # Raymond's
        #apikey = '7SddOmPfjxJu27xUfPzgilmM3P8xTQ3tQmv5C32oCqYn' # Yathu's ?? doesn't work
        apikey = 'SQu0y8zp7XZNk216RxUY-wZuJmuU9A6oV4vSBN0Yjq1_'  # this works
        data = {'grant_type':'urn:ibm:params:oauth:grant-type:apikey', 'apikey':apikey}
        server = "https://iam.bluemix.net/oidc/token"
        IBM_cloud_IAM_uid = "bx"
        IBM_cloud_IAM_pw = "bx"
        auth = (IBM_cloud_IAM_uid, IBM_cloud_IAM_pw)
        response = requests.post(server, headers=headers, data=data, auth=auth) 
        response_json = json.loads(response.text)
        print("response_json = " + str(response_json))
        access_token = response_json['access_token'] 
        print("access token = " + access_token)
        return access_token

def get_ml_instance_id():
    # return "54369f40-6048-478f-ba00-5c1653af7aa6" # Raymond's
    return "e3ac4a09-8322-48a8-b5ab-95ecc4d0924e" # Yathu's

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
    url = 'https://us-south.ml.cloud.ibm.com/v4/deployments/8adaddce-b306-49c1-8853-c6e1ce8cb6fb/predictions'
    return url

def construct_header(iam_token, ml_instance_id):
    header = {'Content-Type': 'application/json', 
              'Authorization': 'Bearer ' + iam_token, 
              'ML-Instance-ID': ml_instance_id}
    return header

def getPrediction(input_payload):
    ml_instance_id  = get_ml_instance_id()
    iam_token = generate_iam_token()
    #print("iam_token = ", iam_token)
    header = construct_header(iam_token, ml_instance_id)
    payload = input_payload
    url = get_server_url()

    response = requests.post(url, json=payload, headers=header)
    context = json.loads(response.text)
    #print("context = ", context)
    #context = {}
    return context

        
def receive(request):
    if (request.method == 'POST'):
            print("In receive: got post request")
            form = FieldsForm(request.POST)
            context = {}
            if form.is_valid():
                print("The form was valid.")
                d1 = form.cleaned_data['d1']
                t1 = form.cleaned_data['t1']
                conf1 = form.cleaned_data['conf1']
                rec1 = form.cleaned_data['rec1']
                dth1 = form.cleaned_data['dth1']
                un1 = form.cleaned_data['un1']
                gas1 = form.cleaned_data['gas1']
                dies1 = form.cleaned_data['dies1']
                print("d1 = %f" % Decimal(d1))
                print("t1 = %f" % Decimal(t1))
                print("conf1 = %d" % Decimal(conf1))
                print("rec1 = %d" % Decimal(rec1))
                print("dth1 = %d" % Decimal(dth1))
                print("un1 = %f" % Decimal(un1))
                print("gas1 = %f" % Decimal(gas1))
                print("dies1 = %f" % Decimal(dies1))

            return redirect('/c19/')
            '''if (request.method == 'POST'):
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
        return HttpResponse(template.render(context, request))'''

def index(request):
    
            
    run_script()
    form = FieldsForm()
    context = {'form': form}
    template = loader.get_template('c19/index.html')
    return HttpResponse(template.render(context, request))

   

    
    

    

    