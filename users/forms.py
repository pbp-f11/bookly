from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import Profile

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username']
    
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control my-2 border border-primary-subtle',
                }
            ),
        }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'image',  
            'first_name', 
            'last_name', 
            'address', 
            'phone_number',
            'gender',
            'email'
            ]

        labels = {
            'first_name':'First Name',
            'last_name': "Last Name",
            'phone_number': 'Phone Number'
        }

        widgets = {
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control my-2 me-5 border border-primary-subtle',
                    'required': False
                }

            ),

            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control my-2 border border-primary-subtle',
                    'required': False,
                    'blank': True
                }
            ),

            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control my-2 border border-primary-subtle',
                    'required': False,
                    'blank': True
                }
            ),

            'address': forms.Textarea(
                attrs={
                    'class': 'form-control my-2 border border-primary-subtle',
                    'rows': '2',
                    'required': False,
                    'blank': True
                }
            ),

            'phone_number': forms.TextInput(
                attrs={
                    'class': 'form-control my-2 border border-primary-subtle',
                    'required': False,
                    'blank': True
                }
            ),

            'gender': forms.Select(
                attrs={
                    'class': 'form-control my-2 border border-primary-subtle',
                    'required': False,
                    'blank': True
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control my-2 border border-primary-subtle',
                    'required': False,
                    'blank': True
                }
            ),
        }