import datetime
#
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from .models import Home, Contacto
from .forms import SuscriberForm, ContactForm
from django.views.generic import (
    TemplateView,
    CreateView,
)
from django.views.generic.edit import FormView
from applications.entrada.models import Entry


class HomePageView(TemplateView):
    template_name = "home/index.html"

    
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        # cargamos el home
        context['home'] = Home.objects.latest('created')
        # texto de portada
        context['portada'] = Entry.objects.entrada_en_portada()
        context['entradas_home'] = Entry.objects.entradas_en_home()
        context['entradas_recientes'] = Entry.objects.entradas_recientes()
        # enviamos formulario de suscripcion
        context['form'] = SuscriberForm
        return context
    
    


class SuscriberCreateView(CreateView):
    # guardar los datos en base a que formulario-->
    form_class = SuscriberForm
    success_url = '.'


class ContactCreateView(FormView):
    # guardar los datos en base a que formulario-->
    form_class = ContactForm
    success_url = '.'

    def form_valid(self, form):

        Contacto.objects.create(
            full_name = form.cleaned_data['full_name'],
            email = form.cleaned_data['email'],
            message = form.cleaned_data['message']
        )

        return super(ContactCreateView,self).form_valid(form)
        

               
        