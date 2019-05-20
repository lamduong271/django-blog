from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author', None)
        self.post = kwargs.pop('post', None)
        super().__init__(*args, **kwargs)
    def save(self, commit=True):
        comment=super().save(commit=False) # not saving to database yet
        comment.author=self.author
        comment.post=self.post
        comment.save() #now save to db

    class Meta: # create an input to input model of comment, having only body cuz author anf post auto detect later
        model = Comment
        fields = ["body"]