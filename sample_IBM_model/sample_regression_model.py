#
# TITLE: sample_regression_model.py
#
# DESC: This code is to access IBM cloud sever for a machine learning model created on Watson Studio. This is an 
#       sample to get our feet wet. The compiled model topic is unrelated to our COVID-19 project, but allows us to make 
#       to design our front end while we are still creating our datasets. 

import urllib3, requests, json


# Must generate IAM_token before hand. Must use CURL unix call described in "generateIAM_curl". 
# iam_token expired after 3600 hours. 

iam_token = "eyJraWQiOiIyMDIwMDMyNjE4MjgiLCJhbGciOiJSUzI1NiJ9.eyJpYW1faWQiOiJpYW0tU2VydmljZUlkLWQ3NWQ4NGM4LTYzYjktNDNkYy05MjlkLTFlZGQ2ZmM2MDQ3MSIsImlkIjoiaWFtLVNlcnZpY2VJZC1kNzVkODRjOC02M2I5LTQzZGMtOTI5ZC0xZWRkNmZjNjA0NzEiLCJyZWFsbWlkIjoiaWFtIiwiaWRlbnRpZmllciI6IlNlcnZpY2VJZC1kNzVkODRjOC02M2I5LTQzZGMtOTI5ZC0xZWRkNmZjNjA0NzEiLCJuYW1lIjoid2RwLXdyaXRlciIsInN1YiI6IlNlcnZpY2VJZC1kNzVkODRjOC02M2I5LTQzZGMtOTI5ZC0xZWRkNmZjNjA0NzEiLCJzdWJfdHlwZSI6IlNlcnZpY2VJZCIsImFjY291bnQiOnsidmFsaWQiOnRydWUsImJzcyI6ImZiMjA5YjlmOTk4NjQyYmNiYzFmNTg1ZTViYzgzMWNjIn0sImlhdCI6MTU4NTcwNzUyNywiZXhwIjoxNTg1NzExMTI3LCJpc3MiOiJodHRwczovL2lhbS5jbG91ZC5pYm0uY29tL2lkZW50aXR5IiwiZ3JhbnRfdHlwZSI6InVybjppYm06cGFyYW1zOm9hdXRoOmdyYW50LXR5cGU6YXBpa2V5Iiwic2NvcGUiOiJpYm0gb3BlbmlkIiwiY2xpZW50X2lkIjoiZGVmYXVsdCIsImFjciI6MSwiYW1yIjpbInB3ZCJdfQ.djFbgSj-4oNd9zWaEbhwksQSu-X7pfvsNHrDb31ZV6YXUUmfG4tJk0hXhthQL70hB1Io55Uk2-enTqJu-loZDCsbwwHI300TIH0A7qumAbprfVa54A5lfYOryes_DguQuIjhKbKNw_zJosEyowaEY0v9pfpK35JVIKvdX__cEiByI_ZuKk4Ug6DcJrXgNlCwoNJeQkUvKv-8KYdG3YAS7OCuqqfSK5mcitL1IaO7pocelBumb4A7t_5H5BHjTy9XufgnZ0ONh6FlYY4mSP5UWYL0ntWBBOIRbl0KlY8zLzeiQCtvp_95bz7nAZ5-PLL5DnbRaKxURMAq92PTrWf57g"
ml_instance_id  = "54369f40-6048-478f-ba00-5c1653af7aa6"

# NOTE: generate iam_token and retrieve ml_instance_id based on provided documentation	
header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + iam_token, 'ML-Instance-ID': ml_instance_id}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"fields": ["No", "X1 transaction date", "X2 house age", "X3 distance to the nearest MRT station", "X4 number of convenience stores", "X5 latitude", "X6 longitude"], 
									"values": [[1, 2010.917, 2, 84, 10, 24.98, 121.54]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/v4/deployments/9300bf9d-85c7-4edd-9cba-22f65a748485/predictions', json=payload_scoring, headers=header)
print("Scoring response")
print(json.loads(response_scoring.text))
