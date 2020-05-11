from django import forms


class RegisterForm(forms.Form):
    email = forms.EmailField(label="login_email")
    password1 = forms.CharField(label="login_password1")
    password2 = forms.CharField(label="login_password2")
