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

    def __str__(self):
        return f"Poster:{self.poster} Headline:{self.headline} Content:{self.body} Likes:{self.likes} Timestamp:{self.created}"