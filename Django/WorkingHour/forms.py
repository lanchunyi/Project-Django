from django import forms

class LoginForm(forms.Form):
    user = forms.CharField(max_length=100)
    passwd = forms.CharField(widget = forms.PasswordInput())