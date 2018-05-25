from django import forms


class FileForm(forms.Form):
    file = forms.FileField(label='画像ファイル')

class TextForm(forms.Form):
    text = forms.CharField()

class NameForm(forms.Form):
    name = forms.CharField()
