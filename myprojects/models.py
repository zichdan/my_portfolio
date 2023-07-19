from django.db import models

# Create your models here.


    
class Portfolio(models.Model):
    tittle = models.CharField(max_length=60)
    description = models.TextField()
    img = models.ImageField(upload_to='blog', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.tittle
    