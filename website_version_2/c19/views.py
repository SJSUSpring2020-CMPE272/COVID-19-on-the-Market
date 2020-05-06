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

def index(request):
    context = {}
    template = loader.get_template('base.html')
    return HttpResponse(template.render(context, request))
    #return HttpResponse("Hello, world. You're at the c19 index.")
