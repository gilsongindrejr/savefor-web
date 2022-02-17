from django import forms


class FileForm(forms.Form):
    file = forms.FileField(label='', widget=forms.FileInput(attrs={'class': 'none'}))
