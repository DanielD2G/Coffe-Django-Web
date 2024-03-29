from django.db import models
class Servicio(models.Model):

    title = models.CharField(max_length=255, verbose_name='Titulo')
    subtitle = models.CharField(max_length=200, verbose_name='Subtitulo')
    content = models.TextField(verbose_name='Contenido')
    image = models.ImageField(verbose_name='Imagen', upload_to='services')
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    date_modified = models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación')
    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"

    def __str__(self):
        return self.title
# Create your models here.
