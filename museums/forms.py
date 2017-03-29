from django import forms
from models import Museum

class AddMuseumForm(forms.ModelForm):
    class Meta:
        model = Museum
        fields = ('title', 'country', 'city','description')