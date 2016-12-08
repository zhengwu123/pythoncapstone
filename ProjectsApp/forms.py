from django import forms
from .models import Project
from tinymce.widgets import TinyMCE


class ProjectForm(forms.Form):
    name = forms.CharField(label='Project Name', widget=forms.TextInput, max_length=200,required=False)
    #name = forms.CharField(widget=TinyMCE)
    description = forms.CharField(label='Description', widget=forms.Textarea, max_length=10000,required=False)
    programmingLanguage = forms.CharField(label='Programming Skill. eg JAVA', widget=forms.TextInput, max_length = 200,required=False)
    yearsOfExperience = forms.CharField(label='Working years', widget=forms.TextInput,required=False)
    speciality = forms.CharField(label='Strength', widget=forms.TextInput,max_length=200,required=False)


class UpdateForm(forms.ModelForm):


    class Meta:
        model = Project
        fields = ('name', 'description', 'programmingLanguage', 'yearsOfExperience','speciality')
        widgets = {
            'description': forms.Textarea()
        }