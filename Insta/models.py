from django.db import models
from django.contrib.auth.models import AbstractUser

from django.urls import reverse

from imagekit.models import ProcessedImageField

# Create your models here.
class Post(models.Model):
    title = models.TextField(blank=True, null=True)
    image = ProcessedImageField(
        upload_to='static/images/posts',
        format='JPEG',
        options={'quality':100},
        blank=True,
        null=True
    )

    def get_absolute_url(self): #called when new post saved
        return reverse("post_detail", args=[str(self.id)]) #get url based on name

# Set up a custom user model is recommended. 
# If there are some needs in the future, it's easier to modify the user model and db, than change from AbstractUser to CustomUser
class InstaUser(AbstractUser):
    profile_pic = ProcessedImageField(
        upload_to='static/images/profiles',
        format='JPEG',
        options={'quality':100},
        blank=True,
        null=True
    )