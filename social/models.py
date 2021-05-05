from django.db import models

# Create your models here.
class Social(models.Model):
    key = models.SlugField(verbose_name='Nombre Clave', max_length=50, unique=True)
    name = models.CharField(verbose_name='Red Social', max_length=50)
    url = models.URLField(verbose_name='Enlace', max_length=50, blank=True, null=True)
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    date_modified = models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación')

    class Meta:
        verbose_name = "enlace"
        verbose_name_plural = "enlaces"

    def __str__(self):
        return self.name