from django import forms
from django.forms import ModelForm
from django.forms.widgets import NumberInput

from .models import Question


class QuestionForm(ModelForm):

    choice1 = forms.CharField(max_length=100, required=False)
    choice2 = forms.CharField(max_length=100, required=False)
    choice3 = forms.CharField(max_length=100, required=False)
    choice4 = forms.CharField(max_length=100, required=False)

    pub_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))

    class Meta:
        model = Question
        fields = [
            'question_text',
            'pub_date',
        ]
       