from django.db import models

from apps.accounts.models import User


# Create your models here.

class Story(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media/",null=True,blank=True)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Story'
        verbose_name_plural = 'Stories'  

    def __str__(self):
        return self.title

class LikeComment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    story = models.ForeignKey(Story,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Like(LikeComment):
    
    class Meta:
        verbose_name = "Like"
        verbose_name_plural = "Likes"
        unique_together = ('user', 'story')
    
    def __str__(self):
        return f"{self.user.username} liked {self.story.title}"


class Comment(LikeComment):

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return f"{self.user.username} commented on {self.story.title}"
