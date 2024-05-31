from django import forms
from .models import UserComment

class CommentForm(forms.ModelForm):
    class Meta:
        model = UserComment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'cols': 50})
        }
