from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomUser
from .models import WasteReport

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    
    # Represent radio buttons: "yes" and "no"
    IS_INDIVIDUAL_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    is_individual = forms.ChoiceField(choices=IS_INDIVIDUAL_CHOICES, widget=forms.RadioSelect)
    
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES, required=False)
    id_number = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean(self):
        cleaned_data = super().clean()
        is_individual = cleaned_data.get('is_individual')
        role = cleaned_data.get('role')

        if is_individual == 'yes' and role:
            raise forms.ValidationError("Individuals should not select a role.")
        if is_individual == 'no' and not role:
            raise forms.ValidationError("Non-individuals must select a role (NGO or Authority).")

class WasteReportForm(forms.ModelForm):
    class Meta:
        model = WasteReport
        fields = ['title', 'description', 'category', 'latitude', 'longitude', 'address']
        widgets = {
            'latitude': forms.HiddenInput(attrs={'id': 'id_latitude'}),
            'longitude': forms.HiddenInput(attrs={'id': 'id_longitude'}),
            'address': forms.TextInput(attrs={'readonly': 'readonly', 'id': 'id_address'}),
        }
