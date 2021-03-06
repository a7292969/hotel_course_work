from .models import Comment
from django import forms
from django.contrib.auth.models import User

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'text']
        labels = ['Ваше І\'мя', 'Текст відруку']

    text = forms.CharField(widget=forms.Textarea)
    
