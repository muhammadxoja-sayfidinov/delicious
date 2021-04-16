from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"

    def save(self, commit=True, *args, **kwargs):
        comment = super().save(commit=False)

        if commit:
            comment.save()
        return comment
