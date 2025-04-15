from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from django.utils import timezone

##création de la class

class Post (models.Model):
    
    auteur=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titre=models.CharField(max_length=200)
    texte=models.TextField()
    create_date=models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(blank=True, null=True)
    
    ##les fonctions
    
    def publish(self):
        self.published_date=timezone.now()
        self.save()
     
    def __str__(self):
        return self.titre   
