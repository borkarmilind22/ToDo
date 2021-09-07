from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from app.forms import ToDoForm
from app.models import ToDo
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="login")
def home(request):
     if request.user.is_authenticated:
        user = request.user
        form = ToDoForm()
        todos = ToDo.objects.filter(user=user).order_by('priority')
        return render(request,'index.html', context={'form':form, 'todos': todos})


def login_view(request):
    if request.method=="GET":    
        form = AuthenticationForm()
        context = {"form": form}
        return render (request, 'login.html', context=context)
    
    else:
        form = AuthenticationForm( data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get("password")
            user = authenticate(username = username, password = password)
            print("authenticated", user)
            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            context = {"form": form}
            return render (request, 'login.html', context=context)


def Signup_view(request):
    if request.method=="GET":
        form=UserCreationForm()
        context = {"form":form}
        return render (request, 'signup.html', context=context)

    else: 
        form=UserCreationForm(request.POST) 
        context = {"form":form}
        if form.is_valid():
            user = form. save()
            print(user)
            if user is not None:
                return redirect("login")     
        else:
           return render(request, 'signup.html', context= context)

@login_required(login_url="login")
def add_todo(request):
    if request.user.is_authenticated:
        user = request.user
        form = ToDoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit= False)
            todo.user = user
            todo.save()
            return redirect ("home")    
        else:
            return render(request,'index.html', context={'form':form})


def signout(request):
    logout(request)
    return redirect("login")


def delete_todo(request, id):
    ToDo.objects.get(pk=id).delete()
    return redirect("home")


def change_todo(request, id, status):
    print(id)
    todo = ToDo.objects.get(pk=id)
    todo.status = status
    todo.save()
    return redirect("home")





