from django import forms

from .models import Suscriber, Contacto

class SuscriberForm(forms.ModelForm):

    class Meta:
        model = Suscriber
        fields = {
            'email',
        }

        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Correo Electronico...',
                    'class': 'input-email'
                }
            )
        }

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'
        