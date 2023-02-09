from django import forms
from .models import *

class AddOrkForm(forms.ModelForm):
    class Meta:
        model = Orc
        fields = "__all__"

class RemOrkForm(forms.Form):
    model = Orc
    title = forms.CharField(max_length=100)
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if Orc.objects.filter(title=title).exists():
            return title
        else:
            raise forms.ValidationError('Такого Орка нет в базе')