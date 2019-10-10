from django.shortcuts import render, redirect
from .models import Users, Posts, Comments
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
    acct = Users.objects.get(pk=1)
    try: 
        if request.method == "POST":
            postpost = request.POST.dict()
            title = postpost["title"]
            url =  postpost["url"]
            text = postpost["text"]
            post = Posts(author=acct, title=title, url=url, body=text)
            post.save()
            return redirect("home")
    except:
        return redirect("create_post")
    
def view_post(request):
    #acct_id = request.sessions.get("acct_id")
    acct = Users.objects.get(pk=2)
    all_posts = Posts.objects.all()
    post_counter = 1 
    print("UP HEREEEEEEE::   ", all_posts[0].author)
    print("Actual:   ", acct)
    context = {"account": acct, "all_posts": all_posts, "post_counter": post_counter}
    return render(request, 'home.html', context)

def view_one_post(request, slug):
    #acct = request.sessions.get("acct_id")
    acct = Users.objects.get(pk=2)
    print("This is account:::: ", acct)
    print("This is slug:::::    ", slug)
    post = Posts.objects.get(pk=slug)
    context = {"post": post, "account": acct}
    print("This is CONTEXT;;;;;    ", context)
    return render(request, 'post.html', context)

def delete_post(request, post_id):
    #acct_id = request.sessions.get("acct_id")
    acct = Users.objects.get(pk=1)
    post = Posts.objects.get(pk=post_id)
    context = {"acct": acct, "post": post}
    return render(request, "delete_posts.html", context)

def delete_post_action(request, post_id):
    #acct_id = request.sessions.get("acct_id")
    #acct = Users.objects.get(pk=1)
    post = Posts.objects.get(pk=post_id)
    post.delete()
    return redirect("home")

def newest(request):
    acct = Users.objects.get(pk=1)
    all_posts = Posts.objects.all().order_by('-created_at')
    post_counter = 1 
    context = {"account": acct, "all_posts": all_posts, "post_counter": post_counter}
    return render(request, 'home.html', context)

