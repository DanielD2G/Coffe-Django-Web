from django.db import models

# Create your models here.
class Page(models.Model):
    title = models.CharField(verbose_name='Title', max_length=50)
    content = models.TextField(verbose_name='Contenido')
    order = models.SmallIntegerField(verbose_name='Orden', default=0)
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    date_modified = models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación')

    class Meta:
        verbose_name = "pagina"
        verbose_name_plural = "paginas"
        ordering = ('order', 'title')

    def __str__(self):
        return self.title