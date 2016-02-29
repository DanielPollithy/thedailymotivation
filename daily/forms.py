# In forms.py...
from django import forms

class UploadFileForm(forms.Form):
    uploadImage = forms.FileField(
        label='Select an image',
        help_text='max.20 megabytes'
    )
