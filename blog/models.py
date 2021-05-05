from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    date_modified = models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación')

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"

    def __str__(self):
        return self.name

class Post(models.Model):
    title= models.CharField(max_length=100, verbose_name="Titulo")
    content= models.TextField(verbose_name='Contenido')
    published= models.DateTimeField(verbose_name='Fecha de Publicación', default=now)
    image= models.ImageField(verbose_name='Imagen', upload_to='blog', blank=True, null=True)
    author= models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
    categories= models.ManyToManyField(Category, verbose_name='Categorias', related_name='get_post')
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    date_modified = models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación')

    class Meta:
        verbose_name = "entrada"
        verbose_name_plural = "entrada"

    def __str__(self):
        return self.title