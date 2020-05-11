from django import forms 
import datetime
class CSVForm(forms.Form):

    file = forms.FileField(widget=forms.NumberInput(attrs={'class': 'file-upload-input', 'type':'file', 'onchange':'readURL(this);', 'accept':'csv'}), required=False)
    #<input class="file-upload-input" type='file' onchange="readURL(this);" accept=".csv" />