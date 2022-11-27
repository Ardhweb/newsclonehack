from django.db import models

# Create your models here.
from django.contrib.auth.models import User



class LinkU(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    submit_from = models.ForeignKey(User, on_delete=models.CASCADE)
    upvotes = models.ManyToManyField(User, related_name='votes')

    created_at = models.DateTimeField(auto_now_add=True, editable=False)


    