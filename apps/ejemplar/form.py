from django import forms 
from apps.ejemplar.models import Ejemplar

class ejemplarForm(forms.ModelForm):
    class Meta:
        model = Ejemplar

        fields = [

            'codigo',
            'localizacion',
        ]

        labels = {

            'codigo' : 'codigos',
            'localizacion' : 'localizaciones',
        }

        widgets = {
            'codigos' : forms.TextInput(attrs={'class': 'form-control'}),
            'localizaciones' : forms.TextInput(attrs={'class': 'form-control'}),

        }