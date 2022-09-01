from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser):
    pass


class Posts(models.Model):
    poster = models.ForeignKey(User, on_delete=models.PROTECT)
    headline = models.CharField(max_length=100)
    body = models.CharField(max_length=400)
    created = models.DateTimeField(auto_now_add = True, auto_created=True, blank=True)
    likes = models.ManyToManyField(User, blank=True, default=None, related_name="liked")
    
    @property
    def count(self):
        return self.likes.all.count()

#function returns dict of Object, to Key access all values
    def dict(self):
        return self.__dict__


Like_Choices = (
    ("Like","Like"),
    ("Unlike","Unlike")
)
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete =models.CASCADE)
    value= models.CharField(choices=Like_Choices, default= "Like", max_length=20)

    def __str__(self):
        return str(self.post)





#function returns string representation of Object, mostly for Admin - site 
    def __str__(self):
        return f"Poster:{self.poster} Headline:{self.headline} Content:{self.body} Likes:{self.likes} Timestamp:{self.created}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, related_name="profile", on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank =True, null=True)
    birth_date = models.DateField(null = True, blank = True)
    followers = models.ManyToManyField(User, blank = True, related_name="followers")

    def __str__(self):
        return f"User:  {self.user}"

#ADD SIGNAL in order to automatically create a User profile, when a User is created -> signal has to be imported
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

#------------------------------------------------------------------------ receiver tells what to do, when signal is received

