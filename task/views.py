from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TaskForm

# Create your views here.
def list_task(request):
    tasks = Task.objects.all()
    print(tasks)
    return render(request, 'list_task.html',{"tasks": tasks})

def create_task(request):
    task = Task(title=request.POST['title'], description=request.POST['description'])
    task.save()
    return redirect('/task/')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('/task/')


def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username = request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('home')
            
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm(),
                    'error': 'Username already exists'
                    })
                   
        return render(request, 'signup.html', {
                    'form': UserCreationForm(),
                    'error': 'Passwords did not match'
                    })
        
def tasks(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks.html', {'tasks': tasks})

def createTask(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {
            'form': TaskForm()
        })
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'create_task.html', {
            'form': TaskForm(),
            'error': 'Bad data passed in. Try again.'
        })

def signout(request):
        logout(request)
        return redirect('signin')
    
def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            ##'form': AuthenticationForm()
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
            'error': 'Usuario o contraseña incorrectos',
            ##'form': AuthenticationForm(),
        })
        else:
            login(request, user)
            return redirect('home')
        
       