from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=15)
    description = models.TextField()

    
    def __str__(self) -> str:
        return self.name