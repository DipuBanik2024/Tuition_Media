from django import forms
from .models import tutor_request_post

class TutorRequestForm(forms.ModelForm):
    class Meta:
        model = tutor_request_post
        fields = '__all__'
        widgets = {
            'student_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Student Name'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Number'}),
            'medium': forms.Select(attrs={'class': 'form-select'}),
            'student_class': forms.Select(attrs={'class': 'form-select'}),
            'preferred_tutor': forms.Select(attrs={'class': 'form-select'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Expected Salary'}),
            'tutoring_days': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tutoring Days (e.g., Sun, Tue, Thu)'}),
            'district': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'District'}),
            'area': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Area'}),
        }
