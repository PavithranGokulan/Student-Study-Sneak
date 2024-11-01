from django import forms
from .models import Remainder

class RemainderForm(forms.ModelForm):
    class Meta:
        model = Remainder
        fields = ['title','description','date','time']