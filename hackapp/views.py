from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def home(request):
    context = {}# {"posts": Post.objects.all()}
    return render(request, 'hackapp/main.html', context)

def signUp(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, "hackapp/signup.html", {"form": form})

def login(request):
    pass




# Create your views here.
