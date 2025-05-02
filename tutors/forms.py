# tutor/forms.py

from django import forms
from .models import Tutor

class TutorPostForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = '__all__'
        widgets = {
            'profile_picture': forms.FileInput(attrs={'class':'form-control','style':'height:40px; padding:5px;'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Number'}),
            'medium': forms.Select(attrs={'class': 'form-select'}),
            'graduation_info': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Graduation Information'}),
            'institutions': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Institutions'}),
            'experience_years': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Years of Experience'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),
            'tuition_fee': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Tuition Fee (BDT)'}),
            'subjects': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Subjects you teach'}),
            'short_bio': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Short Bio'}),

        }
