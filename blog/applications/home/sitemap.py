from datetime import timedelta, datetime
from django.contrib.sitemaps import Sitemap
from applications.entrada.models import Entry
from django.urls import reverse_lazy, reverse

class EntrySitemap(Sitemap):

    # Con que frecuencia se hacen cambios
    changefreq = 'weekly'
    # Prioridad que van a tener mis paginas
    priority = 0.8
    protocol = 'https'
    
    # de quienes vamos a generar las urls
    def items(self):
        return Entry.objects.filter(public=True)

    # la fecha de la ultima modificacion

    def lastmod(self, obj):
        return obj.created


class Sitemap(Sitemap):

    protocol = 'https'

    def __init__(self, names):
        self.names = names

    def items(self):
        return self.names

    def changefreq(self, obj):
        return 'weekly'
        
    def lastmod(self, obj):
        return datetime.now()

    def location(self, obj):
        return reverse_lazy(obj)