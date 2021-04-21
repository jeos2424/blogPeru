from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    View,
    DeleteView,
)
# Create your views here.

from .models import Usuario
from applications.entrada.models import Entry

class UserPageView(LoginRequiredMixin, ListView):
    template_name = 'favoritos/perfil.html'
    context_object_name = "entradas_user"
    login_url = reverse_lazy('users_app:user-login')
    def get_queryset(self):

        return Usuario.objects.entradas_user(self.request.user)

class AddFavoriteView(LoginRequiredMixin, View):
    login_url = reverse_lazy('users_app:user-login')

    def post(self, request, *args, **kwargs):
        usuario = self.request.user
        entrada = Entry.objects.get(id=self.kwargs['pk'])
        
        Usuario.objects.create(
            user = usuario,
            entry = entrada,
        )

        return HttpResponseRedirect(
            reverse('favoritos_app:fovorite_perfil')
        )

class FavoriteDeleteView(DeleteView):
    model = Usuario
    success_url = reverse_lazy('favoritos_app:fovorite_perfil')