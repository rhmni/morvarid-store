from django import forms


class AddTicketForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'متن پیام شما . . .',
    }))
