



#zoe's ml_instance_id = "f02f8a37-ab7d-4528-ae60-88d678592f0a"
#zoe's apikey = "aLmlEFjJvsAhbJEps8hT56N_00AdGCoza4XbsW00Ldsm"

def getPrediction(iam_token, valueArray):
	import urllib3, requests, json

	ml_instance_id = "f02f8a37-ab7d-4528-ae60-88d678592f0a"

	# NOTE: generate iam_token and retrieve ml_instance_id based on provided documentation	
	header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + iam_token, 'ML-Instance-ID': ml_instance_id}

	# NOTE: manually define and pass the array(s) of values to be scored in the next line
	payload_scoring = {"input_data": [{"fields": ["Adj Close (^GSPC)", "DGS10 [%]", "T10YIE[%]", "Confirmed COVID-19 cases", "Recovered COVID-19 cases", "Deaths due to 							COVID-19 ", "Weekly U.S. All Grades All Formulations Retail Gasoline Prices  (Dollars per Gallon)", "Weekly U.S. No 2 Diesel 							Retail Prices  (Dollars per Gallon)"], 		"values": valueArray}]}

	response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/v4/deployments/2a522dc4-098d-4187-9063-01089fa2db78/predictions', json=payload_scoring, headers=header)
	print("Scoring response")
	print(json.loads(response_scoring.text))

	return response_scoring.json()





def get_Iam_token():
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
