from django.contrib import admin
from .models import Posts, User,UserProfile, Like

# Register your models here.
admin.site.register(Posts)
admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Like)