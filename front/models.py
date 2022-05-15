from django.db import models

# Create your models here.

class SiteInfo(models.Model):
    title = models.CharField(max_length=255)
    main_color = models.CharField(max_length=10)
    full_site_color = models.CharField(max_length=10)
    default_mode = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now=True)
    updeted_at = models.DateTimeField(auto_now_add=True,)
    detedt_at = models.DateTimeField(null= True)
    
    def __str__(self) -> str:
        return self.title
    

class Contact(models.Model):
    face_link = models.URLField(null=True)
    twitter_link = models.URLField(null=True)
    main_phone = models.CharField(max_length=10)
    dial_code = models.CharField(max_length=5)
    email = models.EmailField()
    lat = models.DecimalField(max_digits=12,decimal_places=10)
    lon = models.DecimalField(max_digits=12,decimal_places=10)
    
    created_at = models.DateTimeField(auto_now=True)
    updeted_at = models.DateTimeField(auto_now_add=True,)
    detedt_at = models.DateTimeField(null= True)
    
    def __str__(self) -> str:
        return self.email
    
    
class Slider(models.Model):
    imageOne = models.URLField()
    imageTwo = models.URLField()
    imageFree = models.URLField()
    
    titleOne = models.CharField(max_length=255)
    titleTow = models.CharField(max_length=255)
    titleFree = models.CharField(max_length=255)
    
    created_at = models.DateTimeField(auto_now=True)
    updeted_at = models.DateTimeField(auto_now_add=True,)
    detedt_at = models.DateTimeField(null= True)
    
    def __str__(self) -> str:
        return self.titleOne
    