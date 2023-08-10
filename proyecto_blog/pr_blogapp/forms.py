from django import forms
from pr_blogapp.models import Articulo

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['titulo', 'subtitulo', 'cuerpo', 'imagen']