from django import forms
from .models import Account

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'type': "password"
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'type': "password"
    }))

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'email']

    def clean(self):
        cleaned_data = super(SignupForm, self).clean(   )
        password = cleaned_data['password']
        confirm_password = cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError(
                'Password doesnot match'
            )