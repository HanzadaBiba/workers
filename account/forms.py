from django import forms
from django.contrib.auth.models import User
from workers.models import Departaments
from account.models import Position
# Create your models here.
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',widget=forms.PasswordInput)
    departament = forms.ModelChoiceField(queryset=Departaments.objects.all(),label='Департамент')
    position = forms.ModelChoiceField(queryset=Position.objects.all(),label='Должность')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
        def clean_password2(self):
            cd = self.cleaned_data
            if cd['password'] != cd['password2']:
                raise forms.ValidationError('Passwords don\'t match.')
            return cd['password2']