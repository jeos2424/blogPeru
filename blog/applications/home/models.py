from django.db import models
# apps terceros Modelo con sello de Tiempo
from model_utils.models import TimeStampedModel

# Create your models here.

class Home(TimeStampedModel):

    title = models.CharField(
        'Nombre',
        max_length=30
    )

    description = models.TextField()

    about_title = models.CharField(
        'Titulo Nosotros',
        max_length=50
    )

    about_text = models.TextField()
    
    contact_email = models.EmailField(
        'Email de Contacto',
        blank=True,
        null=True
    )

    phone = models.CharField(
        'Telefono Contacto',
        max_length=20
    )

    class Meta:
        verbose_name = 'Pagina Principal'
        verbose_name_plural = 'Pagina Principal'
    
    def __str__(self):
        return self.title


class Suscriber(TimeStampedModel):

    email = models.EmailField()

    class Meta:
        verbose_name = 'Suscripcion'
        verbose_name_plural = 'Suscripciones'
    
    def __str__(self):
        return self.email


class Contacto(TimeStampedModel):

    full_name = models.CharField(
        'Nombres',
        max_length=50
    )

    email = models.EmailField()

    message = models.TextField()

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Mensajes'
    
    def __str__(self):
        return self.full_name