from django.db import models

# Create your models here.


from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='users/%Y/%m/%d/',blank=True)
    full_name =models.CharField( max_length=50, default="")
    dob = models.DateField(blank=True, null=True)
    phone =models.CharField( max_length=13, default="")
    email =models.EmailField( max_length=250, default="")
    
    
   
    
    def __str__(self):
        return f'Profile for user {self.user.username}'
