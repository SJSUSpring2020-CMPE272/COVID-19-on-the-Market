from django import forms 
import datetime
class FieldsForm(forms.Form):
        key = forms.DateField(label='Date', initial=datetime.date.today)
        dgs = forms.DecimalField(label='dgs') 
        t10 = forms.DecimalField(label='t10') 
        confirmed_cases = forms.IntegerField(label='confirmed_cases')
        recovered_cases = forms.IntegerField(label='recovered_cases')
        deaths = forms.IntegerField(label='deaths')
        unemployment = forms.IntegerField(label='unemployment')
        gas_prices = forms.DecimalField(label='gas_prices')
        diesel_prices = forms.DecimalField(label='diesel_prices')
        