from django import forms
from .models import Program

class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ['name', 'company', 'contents', 'photo_timer']
        widgets = {
            'contents': forms.CheckboxSelectMultiple(),
        }
