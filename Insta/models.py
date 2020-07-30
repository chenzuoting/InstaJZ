from django.db import models
from django.contrib.auth.models import AbstractUser

from django.urls import reverse

from imagekit.models import ProcessedImageField

# Create your models here.
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

    def get_connections(self):
        connections = UserConnection.objects.filter(creator=self)
        return connections

    def get_followers(self):
        followers = UserConnection.objects.filter(following=self)
        return followers

    def is_followed_by(self, user):
        followers = UserConnection.objects.filter(following=self)
        return followers.filter(creator=user).exists()

    def get_absolute_url(self):
        return reverse('profile', args=[str(self.id)])

    def __str__(self):
        return self.username

class UserConnection(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    creator = models.ForeignKey(
        InstaUser,
        on_delete=models.CASCADE,
        related_name="friendship_creator_set")
    following = models.ForeignKey(
        InstaUser,
        on_delete=models.CASCADE,
        related_name="friend_set")

    def __str__(self):
        return self.creator.username + ' follows ' + self.following.username

class Post(models.Model):
    author = models.ForeignKey(
        InstaUser,
        on_delete=models.CASCADE,
        related_name='my_posts'
    )
    title = models.TextField(blank=True, null=True)
    image = ProcessedImageField(
        upload_to='static/images/posts',
        format='JPEG',
        options={'quality':100},
        blank=True,
        null=True
    )

    def get_like_count(self):
        return self.likes.count()

    def get_absolute_url(self): #called when new post saved
        return reverse("post_detail", args=[str(self.id)]) #get url based on name

class Like(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        #related_name: define here so that its foreign key object, post, can visit it  with this name 
        #and get all the connections with current post
        related_name='likes')
    user = models.ForeignKey(
        InstaUser,
        on_delete=models.CASCADE,
        related_name='likes'
    )

    class Meta:
        # Use this in a relation model, determine if we need some unique info 
        # Combination post and user should be unique
        unique_together = ("post", "user")

    # Display as string
    def __str__(self):
        return 'Like: ' + self.user.username + ' likes ' + self.post.title

    
