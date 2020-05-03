# COVID-19 on the Market
Predicting the stock market during a global pandemic. By Raymond Hong, Yathukulan Thayabaran, Zoe Lie, Michaela Molina

## Abstract
1. COVID-19 is an ongoing pandemic currently affecting the entire world. Not only has this virus taken a toll on the population, but it also has massive effects on the economy. In order to contain the virus, people are being forced or are obligated to stop working, thus having a negative chain effect on other businesses. You can imagine the economy suffering in terms of the stock market and employment. Instead of letting this virus take its toll, it is best for us to prepare ourselves from what is impending. 

2. The best way to combat a virus and its adverse affects on us is to understand and predict what is coming. Understanding the trends that come with a dangerous pandemic is the best way to defend ourselves against it, whether if its protecting ourselves from the virus, or protecting ourselves financially. Being able to anticipate the harmful effects will help many people. 

3. This project will utilize technologies such as IBM Watson Machine Studio, Python Libraries Like Pandas for dataset merging, and other Front end frame works. 

Datasets: 

- CA Gas prices https://ww2.energy.ca.gov/almanac/transportation_data/gasoline/retail_gasoline_prices2_cms.html
- Unemployment Claims https://oui.doleta.gov/unemploy/claims.asp
- S&P500 Dataset https://finance.yahoo.com/quote/%5EDJI?p=^DJI
- CoronaVirus Data https://www.kaggle.com/c/covid19-global-forecasting-week-1/data
- CoronaVirus Data https://datahub.io/core/covid-19 

We combined multiple datasets into one large dataset to use to train our model. The reason being is that there is no pregenerated dataset relating the corona virus statistics with the various economic statistics. Thus, in this project, we will have to make our own by stitching together these datasets. We are planning to get our data based on weeks starting in 2020, and do joins on the data to merge them together. 


# Architecture Diagram

![Architecture](CMPE272_Architecture_3.png)

# Technology Stack
#### Model
- IBM Watson Machine Studio
- Pandas
- Python
#### Website
- Django
- HTML/CSS
- AWS EC2
