from django import forms

from store_user.models import User


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'ostan', 'shahr', 'phone', 'avatar', 'address', 'code_meli')
        widgets = {
            'avatar': forms.FileInput(attrs={'class': 'upload'}),
            'phone': forms.NumberInput(attrs={'placeholder': 'خالی'}),
            'ostan': forms.TextInput(attrs={'placeholder': 'خالی'}),
            'shahr': forms.TextInput(attrs={'placeholder': 'خالی'}),
            'address': forms.Textarea(attrs={'placeholder': 'خالی'}),
            'code_meli': forms.NumberInput(attrs={'placeholder': 'خالی'}),
        }

    def clean_ostan(self):
        ostan = self.cleaned_data['ostan']
        if ostan:
            if len(ostan) < 3 or len(ostan) > 25 or not ostan.isalpha():
                raise forms.ValidationError('یک استان معتبر وارد کنید')
        return ostan

    def clean_shahr(self):
        shahr = self.cleaned_data['shahr']
        if shahr:
            if len(shahr) < 3 or len(shahr) > 25 or not shahr.isalpha():
                raise forms.ValidationError('یک استان معتبر وارد کنید')
        return shahr

    def clean_address(self):
        address = self.cleaned_data['address']
        if address:
            if len(address) < 10:
                raise forms.ValidationError('یک آدرس معتبر وارد کنید')
        return address

    def clean_code_meli(self):
        code_meli = self.cleaned_data['code_meli']
        if code_meli:
            if len(code_meli) < 10:
                raise forms.ValidationError('کد ملی کوتاه است')
        return code_meli

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if phone:
            if len(phone) < 10:
                raise forms.ValidationError('شماره تلفن کوتاه است')
        return phone

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if len(first_name) < 3 or len(first_name) > 25 or not first_name.isalpha():
            raise forms.ValidationError('یک نام معتبر وارد کنید')
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if len(last_name) < 3 or len(last_name) > 40 or not last_name.isalpha():
            raise forms.ValidationError('یک نام خانوادگی معتبر وارد کنید')
        return last_name



