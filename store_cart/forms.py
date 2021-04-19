from django import forms


class AddCartItemForm(forms.Form):
    qtyinput = forms.IntegerField(widget=forms.NumberInput(attrs={'value': 1}))


class AddCouponForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'کد تخفیف خود را وارد نمایید . . .'}))
