from django import forms
from .models import Subscriber

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email',
                'required': True
            })
        }