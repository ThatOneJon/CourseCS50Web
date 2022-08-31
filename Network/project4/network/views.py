from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Posts, UserProfile


def index(request):
#Checking if logged in works with request, since the user is saved
    if request.user.is_authenticated:
        posts = Posts.objects.all()
        postDicts =[]
        for _ in posts:
            postDicts.append(_.dict())
    # use the dict() method of Posts on each Object and put em in the postDicts list of dicts
        return render(request, "network/index.html",{
            "posts": posts
        })
    else:
        return render(request, "network/login.html")



def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

#function to write a new Post to the sqlite Database -> if method is post or to show the form to create a post, if not
def newPost(request):
    # only render this view, if the user is logged in! ------------------
    if request.user.is_authenticated:
        if request.method == "POST":
            headlineC = request.POST["headline"]
            content = request.POST["content"]
            current_User = request.user.id
            post = Posts(poster=User.objects.get(id=current_User), headline=headlineC, body= content, created=True)
            post.save()

            return HttpResponseRedirect(reverse("index"))

        else:
            return render(request, "network/newPost.html")

    else:
            return HttpResponseRedirect(reverse("index"))
        #if not logged in -> redirect to index

def profile(request, user):
#USER is the value given from URL -> which is why the link brings you to real profile page

    if request.method == "POST":
        if request.value == "add":
            profile = UserProfile.objects.get(user = request.user)
            profile.followers.add(request.user)

        else:
            profile = UserProfile.objects.get(user = request.user)
            profile.followers.remove(request.user)


    else:

        JPosts = Posts.objects.filter(poster=User.objects.get(username=user))
        #get to return one parameter, use python filter to return multiple -> could user map to use a function on all 
        return render(request, "network/profile.html", {
            "realName":UserProfile.objects.get(user = User.objects.get(username=user)).name,
            #strange query, but it works -> gets id of User with fitting username and finds their name --- namer is the username from url --- fitting user not just currently logged in
            "name":str(user),
            "username":str(request.user),
            #convert both to string, to make them comperable!
            "followers": 0,
            "posts": JPosts
        }) 

def edit(request, post):
    if request.method == "POST":
        y = request.POST["new"]
        x = Posts.objects.get(id = post)
        x.body = y
        x.save()
        return HttpResponseRedirect(reverse("index"))

    else:
        getPost = Posts.objects.get(id=post)
        return render(request, "network/profile.html", {
            "Thispost":getPost,
        })
    


