from django.db import models
from datetime import date
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=100)
    sub_titulo = models.CharField(max_length=300)
    texto_poste = RichTextUploadingField()
    data_post = models.DateField(auto_now_add=False, default=date.today)
    autor_post = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['titulo']