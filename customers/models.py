from pyexpat import model
from statistics import mode
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

class Customer(models.Model):
    ADMIN = "AD"
    AGENT = "AG"
    CLIENT = "CL"
    
    USER_TYPE = [
        (ADMIN,"ADMIN"),
        (AGENT,"AGENT"),
        (CLIENT,"CLIENT")
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    dial_code = models.CharField(max_length=4)
    user_image = models.URLField()
    birth_date = models.DateField(null=True, blank=True)
    user_type = models.CharField(choices=USER_TYPE,max_length=10)
    created_at = models.DateTimeField(auto_now_add=True,)
    updeted_at = models.DateTimeField(auto_now=True)
    detedt_at = models.DateTimeField(null=True)

    @receiver(post_save, sender=User)
    def create_user_customer(sender, instance, created, **kwargs):
        if created:
            Customer.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_customer(sender, instance, **kwargs):
        instance.customer.save()
        

    def __str__(self) -> str:
        return self.user.username
        



class InfoAgent(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name="customer_info_agent")
    biographie = models.TextField()
    fb_link = models.URLField(blank=True,null=True)
    twitter_link = models.URLField(blank=True,null=True)
    insta_link = models.URLField(blank=True,null=True)
    whatsapp_numero = models.CharField(blank=True,null=True,max_length=15)
    linke_link = models.URLField(blank=True,null=True)
    
    created_at = models.DateTimeField(auto_now=True)
    updeted_at = models.DateTimeField(auto_now_add=True,)
    detedt_at = models.DateTimeField(null= True)
    
    def __str__(self):
        return self.customer
    
    