from django import forms
from displayapp.models import UserData
class User(forms.ModelForm):
    class Meta:
        model=UserData
        fields='__all__'
