from django import forms

from .models import ContactUs


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'نام'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'نام خانوادگی'}),
            'email': forms.EmailInput(attrs={'placeholder': 'آدرس ایمیل'}),
            'subject': forms.TextInput(attrs={'placeholder': 'موضوع پیام'}),
            'text': forms.Textarea(attrs={'placeholder': 'متن پیام'}),
        }
