from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=200, label='Email')
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')