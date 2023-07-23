from django.db import models
from django.utils.text import slugify


# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=50)
    
    def __str__(self):
        return self.category

    
class Project(models.Model):
    tittle = models.CharField(max_length=60)
    proj_intro = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField()
    proj_img1 = models.ImageField(upload_to='projects/proj_img1', blank=True, null=True)
    proj_img2 = models.ImageField(upload_to='projects/proj_img2', blank=True, null=True)
    proj_img3 = models.ImageField(upload_to='projects/proj_img3', blank=True, null=True)
    client = models.CharField(max_length=100, default='', blank=True, null=True)  # Provide a default value here
    github_link = models.URLField(max_length=200, default='')  # Provide a default value here
    project_url = models.URLField(max_length=200, default='')  # Provide a default value here
    time_created = models.DateTimeField(auto_now_add=True, blank=True)
    date_created = models.DateField()
    
    category = models.ManyToManyField(Category, blank=True)

    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.tittle
    
    def save(self, *args, **kwargs):
        
        if self.slug == None:
            slug = slugify(self.tittle)
            
            has_slug = Project.objects.filter(slug=slug).exists()
            count = 1
            
            while has_slug:
                count += 1
                slug =slugify(self.tittle) + '-' + str(count)
                has_slug = Project.objects.filter(slug=slug).exists()
            self.slug = slug
        super().save(*args, **kwargs)





class Resume(models.Model):
    tittle = models.CharField(max_length=60)
    file = models.FileField(upload_to='resume', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.tittle
    
 
 
 
 
 
 
# from django.db import models
# from django.utils.text import slugify
# from django.contrib.auth.models import User


# JOB_TYPE = (
#     ('Full Time','Full Time'),
#     ('Part Time','Part Time'),
#     )

# def image_upload(instance,filename):
#     imagename , extension = filename.split(".")
#     return "jobs/%s.%s"%(instance.id,extension)

# # Job table/Entity
# #https://docs.djangoproject.com/en/4.1/ref/models/fields/
# class Job(models.Model):  
#     title        = models.CharField(max_length=100)  
#     job_type     = models.CharField(max_length=15 , choices=JOB_TYPE)
#     description  = models.TextField(max_length=1000)
#     published_at = models.DateTimeField(auto_now=True)
#     vacancy      = models.IntegerField(default=1)
#     salary       = models.IntegerField(default=0)
#     experience   = models.IntegerField(default=1) 
#     image = models.ImageField(upload_to= image_upload)
    
#     # https://docs.djangoproject.com/en/4.1/ref/forms/fields/ 
#     # short label for something, containing only letters, numbers, underscores or hyphens. They’re generally used in URLs.
#     slug = models.SlugField(blank=True, null=True) # https://www.jobboard.com/add-the-slug-field-inside-django-model/
    
#     # Relations
#     category     = models.ForeignKey('Category', on_delete=models.CASCADE, default=1) # one to many
#     owner = models.ForeignKey(User, related_name='job_owner', on_delete=models.CASCADE)
    
#     def save(self,*args, **kwargs):
#         self.slug = slugify(self.title) # slugify will take the title and replace the space with underscore (job-board-software-engineer)
#         super(Job,self).save(*args, **kwargs)
        
        
#     def __str__(self):
#         return self.title
    
#     class Meta:
#         ordering = ['-published_at']
#         db_table = 'jobs_table'
    
# class Category(models.Model):
#     name = models.CharField(max_length=25)

#     def __str__(self):
#         return self.name
    
#     class Meta:
#         db_table = 'category_table'

# # Apply form   
# class Apply(models.Model):
#     name = models.CharField(max_length=50)
#     email = models.EmailField(max_length=100)
#     website = models.URLField()
#     cv = models.FileField(upload_to='apply/')
#     cover_letter = models.TextField(max_length=100000)
#     created_at = models.DateTimeField(auto_now=True)

#     # Relations
#     job = models.ForeignKey(Job, related_name='apply_job', on_delete=models.CASCADE)
    
    
#     def __str__(self):
#         return self.name
    
#     class Meta:
#         db_table = "applications_table"



# # M - models
# # V - views
# # T - templates
   


