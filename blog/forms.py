from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['target_url']

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'