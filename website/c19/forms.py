from django import forms 
import datetime
class FieldsForm(forms.Form):
        #number = forms.CharField(label='Number')
        transaction_date = forms.DateField(label='Date',initial=datetime.date.today)
        house_age = forms.IntegerField(label='House Age')
        distance_to_station = forms.IntegerField(label='Distance to Nearest MRT Station')
        number_of_stores = forms.IntegerField(label='Number of Convenience Stores')
        latitude = forms.DecimalField(label='latitude')
        longitude = forms.DecimalField(label='longitude') 