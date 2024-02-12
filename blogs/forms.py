from django import forms
from blogs.models import CommentModel

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ('name', 'email', 'phone', 'comments')