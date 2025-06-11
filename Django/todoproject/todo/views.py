from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def home(request):
    tasks = Task.objects.all()
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'home.html', {'form': form, 'tasks': tasks})
