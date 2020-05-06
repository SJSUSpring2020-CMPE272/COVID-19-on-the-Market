from django import forms 
import datetime
class FieldsForm(forms.Form):

        '''
        1. d = dgs
        2. t = t10
        3. conf = confirmed_cases
        4. rec = recovered_cases
        5. dth = death
        6. un = enemployment
        7. gas = gas_prices
        8. dies = diesel_prices 
        '''

        # Row 1
        d1 = forms.CharField(widget=forms.NumberInput(attrs={'id': 'd1_range','class': 'slider-range', 'type':'range', 'value': '2.66', 'step': '.01', 'min': '1.00', 'max': '100.00'}), required=False)
        #d1_ = forms.CharField(widget=forms.TextInput(attrs={'class':'value',}), required=False)
        d1_= forms.CharField(max_length=10, widget= forms.TextInput(attrs={'class':'input-value'}))
        t1 = forms.CharField(widget=forms.NumberInput(attrs={'id': 't1_range','class': 'slider-range', 'type':'range', 'value': '1.7', 'step': '.01', 'min': '1.00', 'max': '100.00'}), required=False)
        t1_= forms.CharField(max_length=10, widget= forms.TextInput(attrs={'class':'input-value'}))
        conf1 = forms.CharField(widget=forms.NumberInput(attrs={'id': 'conf1_range','class': 'slider-range', 'type':'range','value': '1000', 'step': '1', 'min': '1', 'max': '1000000'}), required=False)
        conf1_= forms.CharField(max_length=10, widget= forms.TextInput(attrs={'class':'input-value'}))
        rec1 = forms.CharField(widget=forms.NumberInput(attrs={'id': 'rec1_range','class': 'slider-range', 'type':'range', 'value': '200','step': '1', 'min': '1', 'max': '1000000'}), required=False)
        rec1_= forms.CharField(max_length=10, widget= forms.TextInput(attrs={'class':'input-value'}))
        dth1 = forms.CharField(widget=forms.NumberInput(attrs={'id': 'dth1_range','class': 'slider-range', 'type':'range', 'value': '50','step': '1', 'min': '1', 'max': '1000000'}), required=False)
        dth1_= forms.CharField(max_length=10, widget= forms.TextInput(attrs={'class':'input-value'}))
        un1 = forms.CharField(widget=forms.NumberInput(attrs={'id': 'un1_range','class': 'slider-range', 'type':'range','value': '220100.0', 'step': '.01', 'min': '1', 'max': '1000000.0'}), required=False)
        un1_= forms.CharField(max_length=10, widget= forms.TextInput(attrs={'class':'input-value'}))
        gas1 = forms.CharField(widget=forms.NumberInput(attrs={'id': 'gas1_range','class': 'slider-range', 'type':'range', 'value': '2.329','step': '.001', 'min': '1', 'max': '25.000'}), required=False)
        gas1_= forms.CharField(max_length=10, widget= forms.TextInput(attrs={'class':'input-value'}))
        dies1 = forms.CharField(widget=forms.NumberInput(attrs={'id': 'dies1_range','class': 'slider-range', 'type':'range', 'value': '3.013','step': '.001', 'min': '1', 'max': '25.000'}), required=False)
        dies1_= forms.CharField(max_length=10, widget= forms.TextInput(attrs={'class':'input-value'}))
        file = forms.FileField()
        #d1    = forms.DecimalField(label='d1') 
        #t1    = forms.DecimalField(label='t1') 
        #conf1 = forms.IntegerField(label='conf1')
        #rec1  = forms.IntegerField(label='rec1') 
        #dth1  = forms.IntegerField(label='dth1')
        #un1   = forms.IntegerField(label='un1')
        #gas1  = forms.DecimalField(label='gas1')
        #dies1 = forms.DecimalField(label='dies1')
        #sel1  = forms.BooleanField(label='sel1')

        # Row 2
        '''d2    = forms.DecimalField(label='d2') 
        t2    = forms.DecimalField(label='t2') 
        conf2 = forms.IntegerField(label='conf2')
        rec2  = forms.IntegerField(label='rec2') 
        dth2  = forms.IntegerField(label='dth2')
        un2   = forms.IntegerField(label='un2')
        gas2  = forms.DecimalField(label='gas2')
        dies2 = forms.DecimalField(label='dies2')
        sel2  = forms.BooleanField(label='sel2')

        # Row 3
        d3    = forms.DecimalField(label='d3') 
        t3    = forms.DecimalField(label='t3') 
        conf3 = forms.IntegerField(label='conf3')
        rec3  = forms.IntegerField(label='rec3') 
        dth3  = forms.IntegerField(label='dth3')
        un3   = forms.IntegerField(label='un3')
        gas3  = forms.DecimalField(label='gas3')
        dies3 = forms.DecimalField(label='dies3')
        sel3  = forms.BooleanField(label='sel3')

        # Row 4
        d4    = forms.DecimalField(label='d4') 
        t4    = forms.DecimalField(label='t4') 
        conf4 = forms.IntegerField(label='conf4')
        rec4  = forms.IntegerField(label='rec4') 
        dth4  = forms.IntegerField(label='dth4')
        un4   = forms.IntegerField(label='un4')
        gas4  = forms.DecimalField(label='gas4')
        dies4 = forms.DecimalField(label='dies4')
        sel4  = forms.BooleanField(label='sel4')

        # Row 5
        d5    = forms.DecimalField(label='d5') 
        t5    = forms.DecimalField(label='t5') 
        conf5 = forms.IntegerField(label='conf5')
        rec5  = forms.IntegerField(label='rec5') 
        dth5  = forms.IntegerField(label='dth5')
        un5   = forms.IntegerField(label='un5')
        gas5  = forms.DecimalField(label='gas5')
        dies5 = forms.DecimalField(label='dies5')
        sel5  = forms.BooleanField(label='sel5')

        # Row 6
        d6    = forms.DecimalField(label='d6') 
        t6    = forms.DecimalField(label='t6') 
        conf6 = forms.IntegerField(label='conf6')
        rec6  = forms.IntegerField(label='rec6') 
        dth6  = forms.IntegerField(label='dth6')
        un6   = forms.IntegerField(label='un6')
        gas6  = forms.DecimalField(label='gas6')
        dies6 = forms.DecimalField(label='dies6')
        sel6  = forms.BooleanField(label='sel6')

        #dgs = forms.DecimalField(label='dgs') 
        #t10 = forms.DecimalField(label='t10') 
        #confirmed_cases = forms.IntegerField(label='confirmed_cases')
        #recovered_cases = forms.IntegerField(label='recovered_cases')
        #deaths = forms.IntegerField(label='deaths')
        #unemployment = forms.IntegerField(label='unemployment')
        #gas_prices = forms.DecimalField(label='gas_prices')
        #diesel_prices = forms.DecimalField(label='diesel_prices')'''
        