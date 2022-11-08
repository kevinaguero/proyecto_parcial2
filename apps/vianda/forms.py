from django import forms
from datetime import datetime
from django.core.exceptions import ValidationError
from django.forms import DateInput

from .models import InfoSolicitudVianda

#formato del formulario para solicitar una vianda
class InfoSolicitudViandaForm(forms.ModelForm):
    class Meta:
        model = InfoSolicitudVianda
        fields = ('tipoMenu', 'frecuencia', 'fechaInicioVianda', 'cantidadViandas','itemsincluir')

        widgets = {
            'fechaInicioVianda': DateInput(format='%Y-%m-%d', attrs={'type': 'date'})
        }

    # def clean(self):
    #     cleaned_data = super().clean()
    #     fechaActual = self.cleaned_data['fechaInicioVianda']
    #     fechaInicioVianda = self.cleaned_data['fechaInicioVianda']
    #     # Verifica que la fecha de inicio sea posterior a la fecha actual
    #     if fechaInicioVianda > fechaActual:
    #         raise ValidationError(
    #             {'fecha_inicio': 'La Fecha de Inicio no puede ser posterior que la fecha actual'},
    #             code='invalido'
    #         )
    #     return cleaned_data
