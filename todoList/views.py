from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task


# Create your views here.
def addTask(request):
    task = request.POST['task']   
    Task.objects.create(task=task)
    return redirect('home')


def mark_as_done(request, id):
    task = Task.objects.get(pk=id)
    task.is_completed = True
    task.save()
    return redirect('home')

def undo_mark_as_done(request, id):
    task = Task.objects.get(pk=id)
    task.is_completed = False
    task.save()
    return redirect('home')


def edit_task(request, id):
    get_task = Task.objects.get(pk=id)
    if request.method == "POST":
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect('home')
    else:
        context = {
            'get_task': get_task
        }
    return render(request, 'edit_task.html', context)

def delete_task(request, id):
    task = Task.objects.get(pk=id)
    task.delete()
    return redirect('home')
