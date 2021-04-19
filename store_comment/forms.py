from django import forms

from .models import Comment


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

        widgets = {
            'text': forms.Textarea(attrs={
                'placeholder': 'متن نظر شما . . .'
            })
        }


class AddReplyCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

        widgets = {
            'text': forms.Textarea(attrs={
                'placeholder': 'متن نظر شما . . .'
            })
        }
