from django.shortcuts import render, redirect
from .models import Posts, Comments
from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from . form import UserCreationFormSpec
import requests
# Create your views here.

#Lorenzo's 

def welcome(request):
    return render(request, 'welcome.html')

def create_post(request):
    """
    acct_id = request.session.get("acct_id")
    if not acct_id:
        return redirect("login")
    acct = Users.objects.get(id=acct_id)
    context = {"acct": acct} 
    """
    return render(request, "create_posts.html")

def create_post_action(request):
    #acct_id = request.sessions.get("acct_id")
    print("USER OBJECTS::: ", request.user)
    print("sessions::", request)
    if request.user.is_authenticated:
        current_user = request.user
        acct = User.objects.get(id=current_user.id)
        print("ALL USER OBJECTS::   ", acct.id)
        #try: 
        if request.method == "POST":
            postpost = request.POST.dict()
            print("PostPost:    ", postpost) 
            title = postpost["title"]
            url =  postpost["url"]
            text = postpost["text"]
            post = Posts.objects.create(author=acct, title=title, url=url, body=text)
            post.save()
            print("final post:   ", post)
            return redirect("home")
        #except:
            #return redirect("create_post")
    
def view_post(request):
    #acct_id = request.sessions.get("acct_id")
    acct = request.user
    all_posts = Posts.objects.all()
    post_counter = 1 
    print("UP HEREEEEEEE::   ", all_posts[5].author)
    print("Actual:   ", acct)
    context = {"account": acct, "all_posts": all_posts, "post_counter": post_counter}
    return render(request, 'home.html', context)

def newest(request):
    acct = Users.objects.get(pk=1)
    all_posts = Posts.objects.all().order_by('-created_at')
    post_counter = 1 
    context = {"account": acct, "all_posts": all_posts, "post_counter": post_counter}
    return render(request, 'home.html', context)

def signUp(request):
    if request.method == "POST":
        form = UserCreationFormSpec(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            user = User.objects.get(username=username)
            add_user_perm(user)
            print(user)
            return redirect('login')
    else:
        form = UserCreationFormSpec()
    return render(request, "hackapp/signup.html", {"form": form})

@login_required
def profile(request):
    return render(request, "hackapp/inform.html")

def add_user_perm(user):
    permission = Permission.objects.get(name='Can add posts')
    user.user_permissions.add(permission)
"""
def view_one_post(request, slug):
    #acct = request.sessions.get("acct_id")
    acct = User.objects.get(pk=2)
    print("This is account:::: ", acct)
    print("This is slug:::::    ", slug)
    post = Posts.objects.get(pk=slug)
    context = {"post": post, "account": acct}
    print("This is CONTEXT;;;;;    ", context)
    return render(request, 'post.html', context)

def delete_post(request, post_id):
    #acct_id = request.sessions.get("acct_id")
    acct = User.objects.get(pk=1)
    post = Posts.objects.get(pk=post_id)
    context = {"acct": acct, "post": post}
    return render(request, "delete_posts.html", context)

def delete_post_action(request, post_id):
    #acct_id = request.sessions.get("acct_id")
    #acct = Users.objects.get(pk=1)
    post = Posts.objects.get(pk=post_id)
    post.delete()
    return redirect("home")







# =======
# from django.http import HttpResponse, JsonResponse
# from .models import *
# from django.contrib.auth.models import *
# >>>>>>> 2ee1f479b9a7eed87b45fc7f2594bb678c64e746
"""
# def new_user(req):
#     """displays form for creating new user"""
#     return render(req, 'hackapp/new.html')
    
# def create_user(req):
#     """gets user info in POST"""
#     if req.method == 'POST':
#         new_user = User(username = req.POST["username"], email = req.POST["email"])
#         new_user.set_password(req.POST["password"])
#         new_users = Users.objects.create(user_name=new_user.username, email=new_user.email)
#         new_user.save()
#         new_users.save()
#         return redirect('../..')
#     return redirect('./new')

# def view_user(req, username):
#     """shows a user profile"""
#     if not req.user.is_authenticated:
#         return redirect('login')
#     username = req.user.username
#     context = {"username": username}
#     if "error" in req.GET:
#         context["error"] = req.GET["error"]
#     return render(req, 'user/profile.html', context)

# def delete_user(req, username):
#     """deletes a user"""
#     if req.user.is_authenticated:
#         try:
#             u = User.objects.get(username=username)
#             u.delete()
#             messages.success(request, "user deleted")
#             return redirect('login')
#         except User.DoesNotExist:
#             messages.error(request, "user does not exist")
#             return redirect('delete_user')
#         except Exception:
#             return redirect('delete_user')
#     return redirect('delete_user')
