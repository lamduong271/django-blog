from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta: # create an input to input model of comment, having only body cuz author anf post auto detect later
        model = Comment
        field = ["body"]