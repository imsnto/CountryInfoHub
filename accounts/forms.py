from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        #self.fields['username'].widget.attrs.update({'class': 'input', 'placeholder': 'Username'})
        #self.fields['password'].widget.attrs.update({'class': 'input', 'placeholder': 'Password'})
