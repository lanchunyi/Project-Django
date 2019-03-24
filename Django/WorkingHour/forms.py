from django import forms
from WorkingHour.utils.ldapAuth import ldapAuth

class LoginForm(forms.Form):
    user = forms.CharField(max_length=100)
    passwd = forms.CharField(widget = forms.PasswordInput())

    def clean_user(self):
        user = self.data["user"]
        passwd = self.data["passwd"]
        auth = ldapAuth(user, passwd)

        if(not auth.ldapconn()):
            raise forms.ValidationError("User Verification failed.")
