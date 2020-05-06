import pandas as pd

def convertCSV(fileName):
	f = pd.read_csv(fileName)
	arr = f.values.tolist()

	return arr

