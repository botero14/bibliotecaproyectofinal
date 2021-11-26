from django import forms 
from apps.libro.models import Libro

class libroForm(forms.ModelForm):
    class Meta:
        model = Libro

        fields = [

            'codigo',
            'titulo',
            'isbn',
            'editorial',
            'numeropagina',
        ]

        labels = {

            'codigo' : 'codigos',
            'titulo' : 'titulos',
            'isbn' : 'isbn',
            'editorial' : 'editoriales',
            'numeropagina' : 'numeropaginas',
        }

        widgets = {
            'codigos' : forms.TextInput(attrs={'class': 'form-control'}),
            'titulos' : forms.TextInput(attrs={'class': 'form-control'}),
            'isbn' : forms.TextInput(attrs={'class': 'form-control'}),
            'editoriales' : forms.TextInput(attrs={'class': 'form-control'}),
            'numeropaginas' : forms.TextInput(attrs={'class': 'form-control'}),

        }