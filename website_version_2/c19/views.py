from django.shortcuts import render
from django.http import HttpResponse
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
import COVID19Py
import requests
from .forms import CSVForm
from .forms import sp_form
from .forms import un_form
import random 


#=========================== S&P 500 =========================================================
def create_image_sp(data):
    input_array = []
    for row in data:
        input_array.append(row)
    payload = construct_payload_sp(input_array)
    predictions = getPrediction_sp(payload) 
    #print("***predictions sp = " + str(predictions))
    #predictions = {'predictions': [{'fields': ['prediction'], 'values': [[2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2536.1139892578126], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2536.1139892578126], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2536.1139892578126], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2551.5869873046877], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2551.5869873046877], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2551.5869873046877], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2551.5869873046877], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2551.5869873046877],]}]}
    dataPoints = predictions["predictions"][0]["values"]
    y = np.linspace(1, len(dataPoints), len(dataPoints))
    figure = plt.figure()
    new_plot = figure.add_subplot(111)
    new_plot.plot(y, dataPoints, color="#000000", linewidth=1, markerfacecolor="#000000")
    spines = '#000099'
    new_plot.spines['bottom'].set_color(spines)
    new_plot.spines['top'].set_color(spines) 
    new_plot.spines['right'].set_color(spines)
    new_plot.spines['left'].set_color(spines)
    for axis in ['bottom','left']:
        new_plot.spines[axis].set_linewidth(3)
    for axis in ['top','right']:
        new_plot.spines[axis].set_linewidth(0)
    new_plot.tick_params(axis='x', colors='black')
    new_plot.tick_params(axis='y', colors='black')
    new_plot.set_xlabel('Day')
    new_plot.set_ylabel('S&P 500')
    new_plot.yaxis.label.set_color('black')
    new_plot.xaxis.label.set_color('black') 
    count = random.randint(1,2000)
    filename = 'static/img/graph' + str(count) + '.png'
    plt.savefig(filename)
    print('filename = ', filename)
    return str(count)
def construct_payload_sp(inputArray):
    payload = {"input_data": 
                [
                    {"fields": [
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
def get_ml_instance_id_sp():
    return "e3ac4a09-8322-48a8-b5ab-95ecc4d0924e" 
def get_server_url_sp():
    url = 'https://us-south.ml.cloud.ibm.com/v4/deployments/8adaddce-b306-49c1-8853-c6e1ce8cb6fb/predictions'
    return url
def construct_header_sp(iam_token, ml_instance_id):
    header = {'Content-Type': 'application/json', 
              'Authorization': 'Bearer ' + iam_token, 
              'ML-Instance-ID': ml_instance_id}
    return header
def generate_iam_token_sp():
        headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Accept': 'application/json'}
        apikey = 'SQu0y8zp7XZNk216RxUY-wZuJmuU9A6oV4vSBN0Yjq1_'  
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
def getPrediction_sp(input_payload):
    ml_instance_id  = get_ml_instance_id_sp()
    iam_token = generate_iam_token_sp()
    header = construct_header_sp(iam_token, ml_instance_id)
    payload = input_payload
    url = get_server_url_sp()

    response = requests.post(url, json=payload, headers=header)
    context = json.loads(response.text)
    return context
##=============================== end S&P 500 =======================================

##================================ begin unemployment ============================================
def create_image_un(data):
    input_array = []
    for row in data:
        input_array.append(row)
    token = get_Iam_token_un()
    predictions = getPrediction_un(token, data)
    print("***predictions un = " + str(predictions))
    #print("predictions = " + str(predictions))
    #predictions = {'predictions': [{'fields': ['prediction'], 'values': [[2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2536.1139892578126], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2536.1139892578126], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2536.1139892578126], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2551.5869873046877], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2551.5869873046877], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2551.5869873046877], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2551.5869873046877], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2551.5869873046877],]}]}
    dataPoints = predictions["predictions"][0]["values"]
    y = np.linspace(1, len(dataPoints), len(dataPoints))
    figure = plt.figure()
    new_plot = figure.add_subplot(111)
    new_plot.plot(y, dataPoints, color="#000000", linewidth=1, markerfacecolor="#000000")
    spines = '#000099'
    new_plot.spines['bottom'].set_color(spines)
    new_plot.spines['top'].set_color(spines) 
    new_plot.spines['right'].set_color(spines)
    new_plot.spines['left'].set_color(spines)
    for axis in ['bottom','left']:
        new_plot.spines[axis].set_linewidth(3)
    for axis in ['top','right']:
        new_plot.spines[axis].set_linewidth(0)
    new_plot.tick_params(axis='x', colors='black')
    new_plot.tick_params(axis='y', colors='black')
    new_plot.set_xlabel('Day')
    new_plot.set_ylabel('Unemployment Claims')
    new_plot.yaxis.label.set_color('black')
    new_plot.xaxis.label.set_color('black') 
    #plt.savefig('static/img/un_graph.png')
    count = random.randint(1,2000)
    filename = 'static/img/graph' + str(count) + '.png'
    plt.savefig(filename)
    return str(count)

def getPrediction_un(iam_token, valueArray):
	import urllib3, requests, json

	ml_instance_id = "f02f8a37-ab7d-4528-ae60-88d678592f0a"

	# NOTE: generate iam_token and retrieve ml_instance_id based on provided documentation	
	header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + iam_token, 'ML-Instance-ID': ml_instance_id}

	# NOTE: manually define and pass the array(s) of values to be scored in the next line
	payload_scoring = {"input_data": [{"fields": ["Adj Close (^GSPC)", "DGS10 [%]", "T10YIE[%]", "Confirmed COVID-19 cases", "Recovered COVID-19 cases", "Deaths due to COVID-19 ", "Weekly U.S. All Grades All Formulations Retail Gasoline Prices  (Dollars per Gallon)", "Weekly U.S. No 2 Diesel Retail Prices  (Dollars per Gallon)"], 		"values": valueArray}]}

	response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/v4/deployments/2a522dc4-098d-4187-9063-01089fa2db78/predictions', json=payload_scoring, headers=header)
	print("Scoring response")
	print(json.loads(response_scoring.text))

	return response_scoring.json()
def get_Iam_token_un():
	import requests

	# Paste your Watson Machine Learning service apikey here
	# Use the rest of the code sample as written
	apikey = "aLmlEFjJvsAhbJEps8hT56N_00AdGCoza4XbsW00Ldsm"

	# Get an IAM token from IBM Cloud
	url = "https://iam.bluemix.net/oidc/token" 
	headers = {"Content-Type": "application/x-www-form-urlencoded"}
	data = "apikey=" + apikey + "&grant_type=urn:ibm:params:oauth:grant-type:apikey"
	IBM_cloud_IAM_uid = "bx"
	IBM_cloud_IAM_pwd = "bx"
	response = requests.post(url, headers=headers, data=data, auth=(IBM_cloud_IAM_uid, IBM_cloud_IAM_pwd))
	iam_token = response.json()["access_token"]

	return iam_token
##================================= end unempl ==============================================
## ================================= begin DJ ===============================================

def create_image_dj(data):
    input_array = []
    for row in data:
        input_array.append(row)
    token = get_Iam_token_dj()
    predictions = getPrediction_dj(token, data)
    print("***predictions dj = " + str(predictions))
    #print("predictions = " + str(predictions))
    #predictions = {'predictions': [{'fields': ['prediction'], 'values': [[2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2536.1139892578126], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2536.1139892578126], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2536.1139892578126], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2551.5869873046877], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2551.5869873046877], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2551.5869873046877], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2551.5869873046877], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2521.202978515625], [2551.5869873046877],]}]}
    dataPoints = predictions["predictions"][0]["values"]
    y = np.linspace(1, len(dataPoints), len(dataPoints))
    figure = plt.figure()
    new_plot = figure.add_subplot(111)
    new_plot.plot(y, dataPoints, color="#000000", linewidth=1, markerfacecolor="#000000")
    spines = '#000099'
    new_plot.spines['bottom'].set_color(spines)
    new_plot.spines['top'].set_color(spines) 
    new_plot.spines['right'].set_color(spines)
    new_plot.spines['left'].set_color(spines)
    for axis in ['bottom','left']:
        new_plot.spines[axis].set_linewidth(3)
    for axis in ['top','right']:
        new_plot.spines[axis].set_linewidth(0)
    new_plot.tick_params(axis='x', colors='black')
    new_plot.tick_params(axis='y', colors='black')
    new_plot.set_xlabel('Day')
    new_plot.set_ylabel('Dow Jones Industrial Average')
    new_plot.yaxis.label.set_color('black')
    new_plot.xaxis.label.set_color('black') 
    #plt.savefig('static/img/dj_graph.png')
    count = random.randint(1,2000)
    filename = 'static/img/graph' + str(count) + '.png'
    plt.savefig(filename)
    return str(count)

def getPrediction_dj(iam_token, valueArray):
	import urllib3, requests, json

	ml_instance_id = "c58f4e6b-959e-4a2a-9bfb-48db758859f9"

	# NOTE: generate iam_token and retrieve ml_instance_id based on provided documentation	
	header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + iam_token, 'ML-Instance-ID': ml_instance_id}

	# NOTE: manually define and pass the array(s) of values to be scored in the next line
	payload_scoring = {"input_data": [{"fields": ["DGS10 [%]", "T10YIE[%]", "Confirmed COVID-19 cases", "Recovered COVID-19 cases", "Deaths due to COVID-19 ", "Initial unemployment claims (Seasonally adjusted)", "Weekly U.S. All Grades All Formulations Retail Gasoline Prices  (Dollars per Gallon)", "Weekly U.S. No 2 Diesel Retail Prices  (Dollars per Gallon)"], "values": valueArray}]}

	response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/v4/deployments/924c419d-92a4-4636-ac27-746372089329/predictions', json=payload_scoring, headers=header)
	print("Scoring response")
	print(json.loads(response_scoring.text))

	return response_scoring.json()

def get_Iam_token_dj():
	import requests

	# Paste your Watson Machine Learning service apikey here
	# Use the rest of the code sample as written
	apikey = "GX9C-Ymh0LZ-jN87dZtmFESo2w79u4cqHoVHCkYuHMjy"

	# Get an IAM token from IBM Cloud
	url = "https://iam.bluemix.net/oidc/token" 
	headers = {"Content-Type": "application/x-www-form-urlencoded"}
	data = "apikey=" + apikey + "&grant_type=urn:ibm:params:oauth:grant-type:apikey"
	IBM_cloud_IAM_uid = "bx"
	IBM_cloud_IAM_pwd = "bx"
	response = requests.post(url, headers=headers, data=data, auth=(IBM_cloud_IAM_uid, IBM_cloud_IAM_pwd))
	iam_token = response.json()["access_token"]

	return iam_token

# ================= end DJ ===============================

apikey = "01524620de4ae02c192d0289d1757a85"

c19 = COVID19Py.COVID19(data_source="nyt")

def getUSInfo():
    url = "https://covidtracking.com/api/us"
    r = requests.get(url=url)
    data = r.json()
    return data

def getCAInfo():
    url = "https://covidtracking.com/api/states"
    r = requests.get(url=url)
    data = r.json()
    for state in data:
        if state["state"] == "CA":
            #print("state = ", state)
            return state
    

def getConfirmedCases():
    return c19.getLatest()["confirmed"]

def getDeaths():
    return c19.getLatest()["deaths"]

def getRecovered():
    return c19.getLatest()["recovered"]

def getLatest():
    return c19.getLatest()


def convertCSV(filename):
    f = pd.read_csv(filename)
    arr = f.values.tolist()
    #print("arr = ", arr)
    return arr 
        

def receive_csv(request):
    if (request.method == 'POST'):
            print("In receive: got post request")
            form = CSVForm(request.POST, request.FILES)
            context = {}
            if form.is_valid():
                print("The form was valid.")
                csv = request.FILES['file']
                data = convertCSV(csv)
                rows = len(data)
                request.session['rows'] = rows
                #print("data = ", data)
                count = create_image_sp(data)
                request.session['imagename'] = 'graph'+count+'.png'
            else:
                print("Form was not valid.")
            return redirect('/c19/graph_sp')    

def receive_input_sp(request):
    if (request.method == 'POST'):
            print("In receive: got post request")
            form = sp_form(request.POST, request.FILES)
            context = {}
            value_array = []
            if form.is_valid():
                print("The form was valid.")
                inner = []
                d1 = form.cleaned_data['d1']
                t1 = form.cleaned_data['t1']
                conf1 = form.cleaned_data['conf1']
                rec1 = form.cleaned_data['rec1']
                dth1 = form.cleaned_data['dth1']
                un1 = form.cleaned_data['un1']
                gas1 = form.cleaned_data['gas1']
                dies1 = form.cleaned_data['dies1']
                check1 = form.cleaned_data['check1']
                #print("d1 = %f" % Decimal(d1))
                #print("t1 = %f" % Decimal(t1))
                #print("conf1 = %d" % Decimal(conf1))
                #print("rec1 = %d" % Decimal(rec1))
                #print("dth1 = %d" % Decimal(dth1))
                #print("un1 = %f" % Decimal(un1))
                #print("gas1 = %f" % Decimal(gas1))
                #print("dies1 = %f" % Decimal(dies1))
                inner.extend([d1, t1, conf1, rec1, dth1, un1, gas1, dies1])
                if (check1 == True):
                    value_array.append(inner)
                # row 2
                inner = []
                d2 = form.cleaned_data['d2']
                t2 = form.cleaned_data['t2']
                conf2 = form.cleaned_data['conf2']
                rec2 = form.cleaned_data['rec2']
                dth2 = form.cleaned_data['dth2']
                un2 = form.cleaned_data['un2']
                gas2 = form.cleaned_data['gas2']
                dies2 = form.cleaned_data['dies2']
                check2 = form.cleaned_data['check2']
                inner.extend([d2, t2, conf2, rec2, dth2, un2, gas2, dies2])
                if (check2 == True):
                    value_array.append(inner)
                # row 3
                inner = []
                d3 = form.cleaned_data['d3']
                t3 = form.cleaned_data['t3']
                conf3 = form.cleaned_data['conf3']
                rec3 = form.cleaned_data['rec3']
                dth3 = form.cleaned_data['dth3']
                un3 = form.cleaned_data['un3']
                gas3 = form.cleaned_data['gas3']
                dies3 = form.cleaned_data['dies3']
                check3 = form.cleaned_data['check3']
                inner.extend([d3, t3, conf3, rec3, dth3, un3, gas3, dies3])
                if (check3 == True):
                    value_array.append(inner)
                # end rows
                print("value_array = ", value_array)
                rows = len(value_array)
                request.session['rows'] = rows
                count = create_image_sp(value_array)
                request.session['imagename'] = 'graph'+count+'.png'
            else:
                print("Form was not valid.")

            return redirect('/c19/graph_sp')

def receive_input_dj(request):
    if (request.method == 'POST'):
            print("In receive: got post request")
            form = sp_form(request.POST, request.FILES)
            context = {}
            value_array = []
            if form.is_valid():
                print("The form was valid.")
                inner = []
                d1 = form.cleaned_data['d1']
                t1 = form.cleaned_data['t1']
                conf1 = form.cleaned_data['conf1']
                rec1 = form.cleaned_data['rec1']
                dth1 = form.cleaned_data['dth1']
                un1 = form.cleaned_data['un1']
                gas1 = form.cleaned_data['gas1']
                dies1 = form.cleaned_data['dies1']
                check1 = form.cleaned_data['check1']
                #print("d1 = %f" % Decimal(d1))
                #print("t1 = %f" % Decimal(t1))
                #print("conf1 = %d" % Decimal(conf1))
                #print("rec1 = %d" % Decimal(rec1))
                #print("dth1 = %d" % Decimal(dth1))
                #print("un1 = %f" % Decimal(un1))
                #print("gas1 = %f" % Decimal(gas1))
                #print("dies1 = %f" % Decimal(dies1))
                inner.extend([d1, t1, conf1, rec1, dth1, un1, gas1, dies1])
                if (check1 == True):
                    value_array.append(inner)
                # row 2
                inner = []
                d2 = form.cleaned_data['d2']
                t2 = form.cleaned_data['t2']
                conf2 = form.cleaned_data['conf2']
                rec2 = form.cleaned_data['rec2']
                dth2 = form.cleaned_data['dth2']
                un2 = form.cleaned_data['un2']
                gas2 = form.cleaned_data['gas2']
                dies2 = form.cleaned_data['dies2']
                check2 = form.cleaned_data['check2']
                inner.extend([d2, t2, conf2, rec2, dth2, un2, gas2, dies2])
                if (check2 == True):
                    value_array.append(inner)
                # row 3
                inner = []
                d3 = form.cleaned_data['d3']
                t3 = form.cleaned_data['t3']
                conf3 = form.cleaned_data['conf3']
                rec3 = form.cleaned_data['rec3']
                dth3 = form.cleaned_data['dth3']
                un3 = form.cleaned_data['un3']
                gas3 = form.cleaned_data['gas3']
                dies3 = form.cleaned_data['dies3']
                check3 = form.cleaned_data['check3']
                inner.extend([d3, t3, conf3, rec3, dth3, un3, gas3, dies3])
                if (check3 == True):
                    value_array.append(inner)
                # end rows
                print("value_array = ", value_array)
                rows = len(value_array)
                request.session['rows'] = rows
                count = create_image_dj(value_array)
                request.session['imagename'] = 'graph'+count+'.png'
            else:
                print("Form was not valid.")

            return redirect('/c19/graph_dj')

def receive_input_un(request): 
    if (request.method == 'POST'):
            print("In receive: got post request")
            form = un_form(request.POST, request.FILES)
            context = {}
            value_array = []
            print("errors = ", form.errors)
            if form.is_valid():
                print("The form was valid.")
                inner = []
                g1 = form.cleaned_data['g1']
                d1 = form.cleaned_data['d1']
                t1 = form.cleaned_data['t1']
                conf1 = form.cleaned_data['conf1']
                rec1 = form.cleaned_data['rec1']
                dth1 = form.cleaned_data['dth1']
                gas1 = form.cleaned_data['gas1']
                dies1 = form.cleaned_data['dies1']
                check1 = form.cleaned_data['check1']
                #print("d1 = %f" % Decimal(d1))
                #print("t1 = %f" % Decimal(t1))
                #print("conf1 = %d" % Decimal(conf1))
                #print("rec1 = %d" % Decimal(rec1))
                #print("dth1 = %d" % Decimal(dth1))
                #print("un1 = %f" % Decimal(un1))
                #print("gas1 = %f" % Decimal(gas1))
                #print("dies1 = %f" % Decimal(dies1))
                inner.extend([g1, d1, t1, conf1, rec1, dth1, gas1, dies1])
                if (check1 == True):
                    value_array.append(inner)
                # row 2
                inner = []
                g2 = form.cleaned_data['g2']
                d2 = form.cleaned_data['d2']
                t2 = form.cleaned_data['t2']
                conf2 = form.cleaned_data['conf2']
                rec2 = form.cleaned_data['rec2']
                dth2 = form.cleaned_data['dth2']
                gas2 = form.cleaned_data['gas2']
                dies2 = form.cleaned_data['dies2']
                check2 = form.cleaned_data['check2']
                inner.extend([g2, d2, t2, conf2, rec2, dth2, gas2, dies2])
                if (check2 == True):
                    value_array.append(inner)
                # row 3
                inner = []
                g3 = form.cleaned_data['g3']
                d3 = form.cleaned_data['d3']
                t3 = form.cleaned_data['t3']
                conf3 = form.cleaned_data['conf3']
                rec3 = form.cleaned_data['rec3']
                dth3 = form.cleaned_data['dth3']
                gas3 = form.cleaned_data['gas3']
                dies3 = form.cleaned_data['dies3']
                check3 = form.cleaned_data['check3']
                inner.extend([g3, d3, t3, conf3, rec3, dth3, gas3, dies3])
                if (check3 == True):
                    value_array.append(inner)
                # end rows
                print("value_array = ", value_array)
                rows = len(value_array)
                request.session['rows'] = rows
                count = create_image_un(value_array)
                request.session['imagename'] = 'graph'+count+'.png'

            else:
                print("Form was not valid.")

            return redirect('/c19/graph_un')


def receive_csv_dj(request):
    if (request.method == 'POST'):
            print("In receive: got post request")
            form = CSVForm(request.POST, request.FILES)
            context = {}
            if form.is_valid():
                print("The form was valid.")
                csv = request.FILES['file']
                data = convertCSV(csv)
                rows = len(data)
                request.session['rows'] = rows
                #print("data = ", data)
                count = create_image_dj(data)
                request.session['imagename'] = 'graph'+count+'.png'
            else:
                print("Form was not valid.")
            return redirect('/c19/graph_dj')    

def receive_csv_un(request):
    if (request.method == 'POST'):
            print("In receive: got post request")
            form = CSVForm(request.POST, request.FILES)
            context = {}
            if form.is_valid():
                print("The form was valid.")
                csv = request.FILES['file']
                data = convertCSV(csv)
                rows = len(data)
                request.session['rows'] = rows
                #print("data = ", data)
                count = create_image_un(data)
                request.session['imagename'] = 'graph'+count+'.png'
            else:
                print("Form was not valid.")
            return redirect('/c19/graph_un')    

def index(request):
    context = {}
    template = loader.get_template('base.html') 
    #context = {
    #    "us": {
    #        "confirmed": getConfirmedCases(),
    #        "deaths": getDeaths(),
    #        "recovered": getRecovered(),
    #    }
    #}
    context = {
        "us": {
            "tests": getUSInfo()[0]['totalTestResults'],
            "confirmed": getUSInfo()[0]['positive'],
            "deaths": getUSInfo()[0]['death'],
            "icu": getUSInfo()[0]['inIcuCurrently']
        },
        "ca": {
            "tests": getCAInfo()['totalTestResults'],
            "confirmed":getCAInfo()['positive'],
            "deaths":getCAInfo()['death'],
            "icu":getCAInfo()['inIcuCurrently']
        }
    }
    #print("confirmed cases = %d" % getConfirmedCases())
    #print("getLatest() = ", getLatest())
    return HttpResponse(template.render(context, request))
   
   

def login(request):
    context = {}
    template = loader.get_template('login.html')
    return HttpResponse(template.render(context, request))

def form(request):
    context = {}
    template = loader.get_template('form.html')
    return HttpResponse(template.render(context, request))

def prediction_sp(request):
    csvform = CSVForm()
    inputform = sp_form()
    context = {'csvform': csvform, 'inputform': inputform}
    template = loader.get_template('prediction_sp.html')
    return HttpResponse(template.render(context, request))

def prediction_dj(request):
    csvform = CSVForm()
    inputform = sp_form()
    context = {'csvform': csvform, 'inputform': inputform}
    template = loader.get_template('prediction_dj.html')
    return HttpResponse(template.render(context, request))

def graph_sp(request):
    context = {}
    template = loader.get_template('graph_sp.html')
    return HttpResponse(template.render(context, request))

def graph_dj(request):
    context = {}
    template = loader.get_template('graph_dj.html')
    return HttpResponse(template.render(context, request))

def prediction_un(request):
    csvform = CSVForm()
    inputform = un_form()
    context = {'csvform': csvform, 'inputform':inputform}
    template = loader.get_template('prediction_un.html')
    return HttpResponse(template.render(context, request))

def graph_un(request):
    context = {}
    template = loader.get_template('graph_un.html')
    return HttpResponse(template.render(context, request))

def buttons(request):
    context = {}    
    template = loader.get_template('buttons.html')
    return HttpResponse(template.render(context, request))


def cards(request):
    context = {}    
    template = loader.get_template('cards.html')
    return HttpResponse(template.render(context, request))

def register(request):
    context = {}    
    template = loader.get_template('register.html')
    return HttpResponse(template.render(context, request))

def forgotpassword(request):
    context = {}    
    template = loader.get_template('forgot-password.html')
    return HttpResponse(template.render(context, request))

def fourpage(request):
    context = {}    
    template = loader.get_template('404.html')
    return HttpResponse(template.render(context, request))

def blankpage(request):
    context = {}    
    template = loader.get_template('blank.html')
    return HttpResponse(template.render(context, request))

def charts(request):
    context = {}    
    template = loader.get_template('charts.html')
    return HttpResponse(template.render(context, request))

def tables(request):
    context = {}    
    template = loader.get_template('tables.html')
    return HttpResponse(template.render(context, request))

def colors(request):
    context = {}    
    template = loader.get_template('utilities-color.html')
    return HttpResponse(template.render(context, request))

def borders(request):
    context = {}    
    template = loader.get_template('utilities-border.html')
    return HttpResponse(template.render(context, request))

def animations(request):
    context = {}    
    template = loader.get_template('utilities-animation.html')
    return HttpResponse(template.render(context, request))

def other(request):
    context = {}    
    template = loader.get_template('utilities-other.html')
    return HttpResponse(template.render(context, request))



