



#
# TITLE: sample_regression_model.py
#
# DESC: This code is to access IBM cloud sever for a machine learning model created on Watson Studio. This is an
#       sample to get our feet wet. The compiled model topic is unrelated to our COVID-19 project, but allows us to make
#       to design our front end while we are still creating our datasets.


def getPrediction(iam_token, valueArray):
	import urllib3, requests, json

	ml_instance_id = "54369f40-6048-478f-ba00-5c1653af7aa6"
	# NOTE: generate iam_token and retrieve ml_instance_id based on provided documentation	
	header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + iam_token, 'ML-Instance-ID': ml_instance_id}

	# NOTE: manually define and pass the array(s) of values to be scored in the next line
	payload_scoring = {"input_data": [{"fields": ["key_0", "DGS10 [%]", "T10YIE[%]",
										 		"Confirmed COVID-19 cases", "Recovered COVID-19 cases", 
										 		"Deaths due to COVID-19 ", "Initial unemployment claims (Seasonally adjusted)", 
										 		"Weekly U.S. All Grades All Formulations Retail Gasoline Prices  (Dollars per Gallon)", 
												 "Weekly U.S. No 2 Diesel Retail Prices  (Dollars per Gallon)"], 
										"values": valueArray}]}

	response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/v4/deployments/3861dfa6-8e65-48f2-b7a3-9bef448a3ea2/predictions', json=payload_scoring, headers=header)
	print("Scoring response")
	print(json.loads(response_scoring.text))

	return response_scoring.json()


def get_Iam_token():
	import requests

	# Paste your Watson Machine Learning service apikey here
	# Use the rest of the code sample as written
	apikey = "zchGXyAjaMtNldcCjII5EuLdc_xFxkJhagKIc32FHxV_"

	# Get an IAM token from IBM Cloud
	url = "https://iam.bluemix.net/oidc/token"
	headers = {"Content-Type": "application/x-www-form-urlencoded"}
	data = "apikey=" + apikey + "&grant_type=urn:ibm:params:oauth:grant-type:apikey"
	IBM_cloud_IAM_uid = "bx"
	IBM_cloud_IAM_pwd = "bx"
	response = requests.post(url, headers=headers, data=data, auth=(IBM_cloud_IAM_uid, IBM_cloud_IAM_pwd))
	iam_token = response.json()["access_token"]

	return iam_token