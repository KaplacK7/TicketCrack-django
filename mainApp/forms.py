from django import forms
from mainApp.models import Funcion, Ubicacion

class FormVenta(forms.Form):
    LARGO_CODIGO = 9
    VALIDADOR_CODIGO = 37

    id_funcion = forms.CharField(widget=forms.HiddenInput)
    cliente = forms.CharField()
    email = forms.EmailField(required=False)
    entradas = forms.IntegerField(min_value=1, max_value=10)
    codigo = forms.CharField(required=False)
    ubicacion = forms.ModelChoiceField(queryset=Ubicacion.objects.none(), empty_label="Seleccione ubicación")

    def __init__(self, *args, **kwargs):
        funcion_id = kwargs.pop('funcion_id', None)
        super().__init__(*args, **kwargs)

        if funcion_id:
            self.fields['ubicacion'].queryset = Ubicacion.objects.filter(funcion_id=funcion_id)
            self.fields['ubicacion'].label_from_instance = lambda obj: (
                f"{obj.nombre} - ${obj.precio} "
                f"(Disponibles: {obj.asientos_disponibles - obj.asientos_vendidos})"
            )
        # Estilos Bootstrap
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    def clean_entradas(self):
        entradas = self.cleaned_data['entradas']
        ubicacion = self.cleaned_data.get('ubicacion')

        if ubicacion:
            disponibles = ubicacion.asientos_disponibles - ubicacion.asientos_vendidos
            if entradas > disponibles:
                raise forms.ValidationError("No hay tantas entradas disponibles para esta ubicación.")
        
        return entradas

    def clean_codigo(self):
        codigo = self.cleaned_data.get('codigo', '')
        return codigo.strip() if codigo else None
