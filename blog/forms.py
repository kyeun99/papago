from django import forms
from .models import Comment1, Comment2, Comment3

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment1
        fields = ("author", "text")

class DommentForm(forms.ModelForm):
    class Meta:
        model = Comment2
        fields = ("author", "text")

class EommentForm(forms.ModelForm):
    class Meta:
        model = Comment3
        fields = ("author", "text")