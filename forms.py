from django import forms 
from .models import *
  
class ContactDetailForm(forms.ModelForm): 
  
    class Meta: 
        model = contact_details
        fields = ['name', 'profile','mobile_no','address','email'];
