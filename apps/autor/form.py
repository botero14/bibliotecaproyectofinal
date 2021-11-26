from django import forms 
from apps.autor.models import Autor

class autorForm(forms.ModelForm):
    class Meta:
        model = Autor

        fields = [

            'nombre',
            'codigo',
        ]

        labels = {

            'nombre' : 'nombres',
            'codigo' : 'codigos',
        }

        widgets = {
            'nombre' : forms.TextInput(attrs={'class': 'form-control'}),
            'codigo' : forms.TextInput(attrs={'class': 'form-control'}),

        }