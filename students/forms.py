from django import forms
from .models import tutor_request_post

class TutorRequestForm(forms.ModelForm):
    class Meta:
        model = tutor_request_post
        fields = '__all__'
