from django import forms
from form_app.models import *

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = '__all__'