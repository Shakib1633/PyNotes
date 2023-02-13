from django import forms
from django.forms import ModelForm
from . models import Notes

class NotesForm(ModelForm):
    heading = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Enter Title", "style":"background: #FFFFCC"} ) )
    text = forms.CharField(max_length=500, widget=forms.Textarea(attrs={"class": "form-control", "placeholder":"Enter Notes", "rows":"8", "style":"background: #FFFFCC"} ) )

    class Meta:
        model = Notes
        fields = ['heading', 'text']