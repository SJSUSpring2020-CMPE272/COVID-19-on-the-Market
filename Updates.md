# Updates
#### March 29th, 2020

- Found more datasets that would assist in finding economic impact of COVID-19 (Gas and unemployment)

#### March 31th, 2020

- Got an example IBM Watson Model working. Able to use python to call the IBM server to send features, and receive a prediction off of a model created for estimating housing prices. Will use this for front-end developers to start working on a UI while Machine Learning Model is being developed. 

#### April 1st,2020

- Digested the input data from multiple sources and converted it to a readable format by Watson. This was performed through Pandas. This digested data was then discussed with the team. After a team meeting, the apparent the deficencies in the data model were identified.


#### April 3rd,2020

- More data gathered over the past two days was filtered and fed into the digester. The code was adjusted accordingly to perform the task. The new dataset is to be fed to the Machine Learning model. 
- Ran the created dataset through IBM Watson. Got a model that predicts the S&P500 after inputing features like DGS10, T10YIE, Confirmed Covid cases, Recovered Covid cases, Deaths due to COVID, unemployment claims, average gas prices, average diesal prices.

#### April 5th, 2020
- Put together boilerplate for website using Django. Website is able to make a request for a new access token and use it to request a prediction from machine learning server. The next step is to incorporate user input. 

#### April 12th, 2020
- Website has a form and is able to handle user input. The next step is to use it as input to the request to the machine learning server. 

#### April 13th, 2020
- Created a python script to utilize  Watson API to automate Token generation and to submit features for predictions. Graph can be generated to show results of predictions.

#### April 17th, 2020
- Website takes form data, makes request to machine learning server, and displays a prediction. 
