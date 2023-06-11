from django import forms
from .models import *

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','email','content']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Введите имя'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Введите почту'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }

class PostForm(forms.ModelForm):
    image = forms.ImageField()
    class Meta:
        model = Post
        fields = ['name','description','image','category','author']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название поста'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя'}),
            'description': forms.Textarea(attrs={'class': 'form-control','placeholder': '...'}),
        }