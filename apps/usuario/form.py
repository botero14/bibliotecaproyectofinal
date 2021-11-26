from django import forms 
from apps.usuario.models import Usuario

class usuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario

        fields = [

            'codigo',
            'nombre',
            'direccion',
            'telefono',
        ]

        labels = {

            'codigo' : 'codigos',
            'nombre' : 'nombres',
            'direccion' : 'direcciones',
            'editorial' : 'editoriales',
            'telefono' : 'telefonos',
        }

        widgets = {
            'codigos' : forms.TextInput(attrs={'class': 'form-control'}),
            'nombres' : forms.TextInput(attrs={'class': 'form-control'}),
            'direcciones' : forms.TextInput(attrs={'class': 'form-control'}),
            'telefonos' : forms.TextInput(attrs={'class': 'form-control'}),

        }