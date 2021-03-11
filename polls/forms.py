from django import forms
from django.forms import ModelForm
from django.forms.widgets import NumberInput

from .models import Question

class QuestionForm(ModelForm):

    choice1 = forms.CharField(max_length=100, required=False, label="Choice 1", widget=forms.TextInput(attrs={'class': 'form-control'}))
    choice2 = forms.CharField(max_length=100, required=False, label="Choice 2", widget=forms.TextInput(attrs={'class': 'form-control'}))
    choice3 = forms.CharField(max_length=100, required=False, label="Choice 3", widget=forms.TextInput(attrs={'class': 'form-control'}))
    choice4 = forms.CharField(max_length=100, required=False, label="Choice 4", widget=forms.TextInput(attrs={'class': 'form-control'}))

    pub_date = forms.DateField(widget=NumberInput(attrs={'type': 'date', 'class': 'form-control'}), label="Date")
    question_text = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Question")

    class Meta:
        model = Question
        fields = [
            'question_text',
            'pub_date',
        ]