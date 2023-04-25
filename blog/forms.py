from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', ]

    def save(self, article, author):
        comment = super().save(commit=False)
        comment.article = article
        comment.user = author
        comment.save()
        return comment
