from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    repeat_password = forms.CharField(
        label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_repeat_password(self):
        cleaned_data = self.cleaned_data
        if cleaned_data['password'] != cleaned_data['repeat_password']:
            raise forms.ValidationError("Password doesn't match")
        return cleaned_data['password']
