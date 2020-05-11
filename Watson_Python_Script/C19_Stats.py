import COVID19Py

# Data source from NYTs
c19 = COVID19Py.COVID19(data_source="nyt")


def getStatsUS(confOrDeaths):
	#confOrDeath must be string equal to 'confirmed' or 'deaths'
	return c19.getLatest()[confOrDeaths]	

def getStatsCounty(id, confOrDeaths):
	# Contra Costa 33
	# Alameda 22
	# Santa Clara 5
	# Napa 18
	# Sonoma 19

	#confOrDeath must be string equal to 'confirmed' or 'deaths'
	countyData = c19.getLocations(rank_by='recovered')[id]
	return countyData['latest'][confOrDeaths]

if __name__ == '__main__':
	print(getStatsCounty(33, 'confirmed'))