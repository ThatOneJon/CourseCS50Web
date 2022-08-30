from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Posts(models.Model):
    poster = models.ForeignKey(User, on_delete=models.PROTECT)
    headline = models.CharField(max_length=100)
    body = models.CharField(max_length=400)
    likes = models.IntegerField(null=True, default = 0)
    created = models.DateTimeField(auto_now_add = True, auto_created=True, blank=True)

#function returns dict of Object, to Key access all values
    def dict(self):
        return self.__dict__


#function returns string representation of Object, mostly for Admin - site 
    def __str__(self):
        return f"Poster:{self.poster} Headline:{self.headline} Content:{self.body} Likes:{self.likes} Timestamp:{self.created}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, related_name="profile", on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank =True, null=True)
    birth_date = models.DateField(null = True, blank = True)
    followers = models.ManyToManyField(User, blank = True, related_name="followers")