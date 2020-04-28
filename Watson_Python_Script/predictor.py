import WatsonCalls
import numpy as np
import matplotlib.pyplot as plt

def predict(arr):
	token = WatsonCalls.get_Iam_token()
	predictions = WatsonCalls.getPrediction(token, arr)
	dataPoints = predictions["predictions"][0]["values"]

	return dataPoints





def createGraph(dataPoints):
	x = np.linspace(1, len(dataPoints), len(dataPoints))
	plt.plot(x, dataPoints)
	plt.savefig('Graph.png')







if __name__ == "__main__":
	predictValues = predict([[2.66, 1.7, 1000, 200, 50, 220100.0, 2.329, 3.013],
         						 [0.73,0.73,4632,17,85,3307000,2.343,2.733],
        							  [0.76,1,959,8,28,282000,2.343,2.733],
       									   [0.92,0.75,19100,147,244,3307000,2.217,2.659],
          										[0.72,0.94,121478,1072,2026,6648000,2.103,2.586]])
	createGraph(predictValues)