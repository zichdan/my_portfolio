from django.db import models

# Create your models here.



class Portfolio(models.Model):
    tittle = models.CharField(max_length=60)
    description = models.TextField()
    proj_img = models.ImageField(upload_to='projects', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.tittle