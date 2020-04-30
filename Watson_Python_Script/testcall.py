import WatsonCalls
import numpy as np
token = WatsonCalls.get_Iam_token()
print(token)
initialValue = np.array([ 2.66, 1.7, 0, 0, 0, 220000, 2.329, 3.013])
WatsonCalls.getPrediction(token, [[ 2.66, 1.7, 0, 0, 0, 220000, 2.329, 3.013]])