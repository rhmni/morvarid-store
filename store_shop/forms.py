from django import forms


class SearchForm(forms.Form):
    search = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'دنبال چه چیزی می گردید ؟'})
    )
