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
                print("data = ", data)
            else:
                print("Form was not valid.")
            return redirect('/c19/')    

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
    form = CSVForm()
    context = {'csvform': form}
    template = loader.get_template('prediction_sp.html')
    return HttpResponse(template.render(context, request))
