from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=15)
    description = models.TextField()

    
    def __str__(self):
        return self.name
    
    
class Blogs(models.Model):
    tittle = models.CharField(max_length=60)
    description = models.TextField()
    authname = models.CharField(max_length=15)
    img = models.ImageField(upload_to='blog', blank=True, null=True)
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.tittle
    
    
class Internship(models.Model):
    fullname = models.CharField(max_length=60)
    usn = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    college_name = models.CharField(max_length=100)
    offer_status = models.CharField(max_length=60)
    start_date = models.CharField(max_length=60)
    end_date = models.CharField(max_length=60)
    proj_report = models.CharField(max_length=60)
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return self.usn
    
    
# class About(models.Model):
#     tittle = models.CharField(max_length=60)
#     description = models.TextField()
#     img = models.ImageField(upload_to='about', blank=True, null=True)
#     timeStamp = models.DateTimeField(auto_now_add=True, blank=True)
    
#     def __str__(self):
#         return self.tittle
    
    


            