from django import forms
from .models import Contacto, Obras
from django.contrib.auth.forms import UserCreationForm



class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = ["nombre", "correo" ,"tipo_consulta","mensaje", "avisos"]



class ObrasForm(forms.ModelForm):

    nombre = forms.CharField(min_length=2, max_length=50)
    autor = forms.CharField(min_length=1, max_length=50)
    precio = forms.IntegerField(min_value=1, max_value=2000000)

    class Meta:
        model = Obras
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    pass 