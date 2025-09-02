from django.db import models

# Create your models here.

class BlogCategory(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.nombre

class BlogPost(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    autor = models.ForeignKey(
        UsuarioPersonalizado,
        on_delete=models.SET_NULL,
        null=True
    )
    categoria = models.ManyToManyField(BlogCategory)
    contenido = models.TextField()
    imagen = models.ImageField(
        upload_to='media/blog/',
        null=True,
        blank=True
    )
    es_publicado = models.BooleanField(default=False)
    fecha_publicacion = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    vistas = models.PositiveIntegerField(default=0)
    solo_miembros = models.BooleanField(default=False)
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        ordering = ['-fecha_publicacion']
