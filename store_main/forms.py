from django import forms

from store_setting.models import Newsletter
from store_user.models import User


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'آدرس ایمیل',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'رمز عبور',
    }))


class RegisterForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'آدرس ایمیل',
    }))

    first_name = forms.CharField(min_length=3, widget=forms.TextInput(attrs={
        'placeholder': 'نام',
    }))

    last_name = forms.CharField(min_length=3, widget=forms.TextInput(attrs={
        'placeholder': 'نام خانوادگی',
    }))
    password1 = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={
        'placeholder': 'رمز عبور',
    }))
    password2 = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={
        'placeholder': 'تکرار رمز عبور',
    }))

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        is_exists_user = User.objects.filter(email=email).exists()
        if is_exists_user:
            raise forms.ValidationError('این کاربر قبلا ثبت نام کرده است')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password2 != password1:
            raise forms.ValidationError('رمز های عبور یکی نیست')
        return password1


class NeewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ('email',)

        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'آدرس ایمیل',
                'class': 'form-control',
            })
        }
