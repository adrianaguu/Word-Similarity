from django import forms

class WordForm(forms.Form):
    word = forms.CharField(label='Word', max_length=100)