from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from . form import UserCreationFormSpec

def home(request):
    context = {}# {"posts": Post.objects.all()}
    return render(request, 'hackapp/main.html', context)

def signUp(request):
    if request.method == "POST":
        form = UserCreationFormSpec(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            return redirect('login')
    else:
        form = UserCreationFormSpec()
    return render(request, "hackapp/signup.html", {"form": form})

@login_required
def profile(request):
    return render(request, "hackapp/inform.html")



# =======
# from django.http import HttpResponse, JsonResponse
# from .models import *
# from django.contrib.auth.models import *
# >>>>>>> 2ee1f479b9a7eed87b45fc7f2594bb678c64e746

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