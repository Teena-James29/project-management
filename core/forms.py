from django import forms
from .models import Project,Task, Client

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'assigned_manager': forms.Select(attrs={'class': 'form-control'}),
        }




class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter task title'  }),
           'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter task description',
                'rows': 3  }),
            'project': forms.Select(attrs={
                'class': 'form-control' }),
            'assigned_to': forms.Select(attrs={
                'class': 'form-control' }),
            'status': forms.Select(attrs={
                'class': 'form-control' }),
            'due_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date' }),
            
            
        }
class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['submission_file']
        widgets = {
            'submission_file': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }



class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter client name' }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter client email' }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter phone number'  }),
            'company': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter company name' }),
        }




from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

CustomUser = get_user_model() 

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email') 