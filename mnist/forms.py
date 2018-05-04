from django import forms


class FileForm(forms.Form):
    file = forms.FileField(label='画像ファイル')
