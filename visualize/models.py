from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField() # may need to change the type of model when adding visuals/infographics
    date_posted = models.DateTimeField(default=timezone.now) #auto_now = True for last modified
    author = models.ForeignKey(User, on_delete=models.CASCADE) #if user deleted --> delete their posts but not the other way around

    def __str__(self):
        return self.title