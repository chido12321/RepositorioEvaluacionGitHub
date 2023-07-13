from django import forms
from LibrosApp .models import Libros

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libros
        fields = ['nombre', 'autor', 'descripcion', 'codigo','estado']
        labels = {
            'nombre': 'Nombre',
            'autor': 'autor',
            'descripcion': 'descripcion',
            'codigo': 'codigo',  # Agrega una coma al final de esta línea
            'estado':'estado',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'estado':forms.TextInput(attrs={'class': 'form-control'}),
        }
