from django import forms
from pieces.models import Piece

class AddPieceForm(forms.ModelForm):
    class Meta:
        model = Piece
        fields = ('title', 'description', 'image')
