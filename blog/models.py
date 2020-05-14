from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) #
    title = models.CharField(max_length=200) #CharField texto con longitud limitada
    text = models.TextField()   #TexrField texto con longitud ilimitada
    created_date = models.DateTimeField( #DateTimeField fecha y hora
            default=timezone.now)
    publicar_date = models.DateTimeField(
            blank=True, null=True)

    def publicar(self): #Metodo publicar 
        self.publicar_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
