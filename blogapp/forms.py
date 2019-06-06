from django import forms
from blogapp.models import Users
from blogapp.models import Blogs
# Create your models here.
class UserForm(forms.ModelForm):
    class Meta:
        model=Users
        fields='__all__'

class BlogForm(forms.ModelForm):
    class Meta:
        model=Blogs
        fields=('title','pic','blog')
