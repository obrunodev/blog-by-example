from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):
    
    class Status(models.TextChoices):
        """
        Leituras complementares:
        - https://docs.djangoproject.com/en/4.1/ref/models/fields/#enumeration-types
        
        Usando o models.TextChoices:
        - Escolhas disponíveis: Post.Status.Choices
        - Nomes legíveis: Post.Status.labels (Draft, Published)
        - Valor atual das escolhas: Post.Status.values (DF, PB)
        - Post.Status.names (DRAFT, PUBLISHED)
        """
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)
    
    class Meta:
        ordering = ['-publish']
        # Melhora o desempenho quando filtra ou ordena pelo campo listado.
        indexes = [
            models.Index(fields=['-publish']),
        ]
    
    def __str__(self):
        return self.title
