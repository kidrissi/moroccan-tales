from django.db import models

from apps.accounts.models import User


# Create your models here.

class Story(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media/",null=True,blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title