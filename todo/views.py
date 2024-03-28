from django.shortcuts import get_object_or_404, redirect, render

from todo.models import Task

# Create your views here.
def addTask(request):
    task = request.POST.get('task')
    Task.objects.create(task=task)
    return redirect('home')

def markAsDone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def markAsNotDone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def editTask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.task = request.POST.get('task')
        task.save()
        return redirect('home')
    else:
        context = {
            'task': task
        }
        return render(request, 'editTask.html', context)
    
def deleteTask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')