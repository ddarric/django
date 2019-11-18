from django.shortcuts import render, redirect
from todo_list.models import Task
from todo_list.forms import NewTaskForm
from datetime import date
# Create your views here.


def main_page(request):
    if request.method == 'POST':
        print(request.POST)
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = Task(
                title = form.cleaned_data['title'],
                description = form.cleaned_data['description'],
                end_date = form.cleaned_data['end_date']
            )
            task.save()
    else:
        form = NewTaskForm()
    tasks = Task.objects.all()
    return render(request, 'main_page.html', {'form': form, 'tasks': tasks})

def task_details(request, pk):
    task = Task.objects.filter(pk = pk)
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task.update(title = form.cleaned_data['title'])
            task.update(description = form.cleaned_data['description'])
            task.update(end_date = form.cleaned_data['end_date'])
            return redirect('todo_list:main_page')
    else:
        task = task.first()
        form = NewTaskForm(initial = {
            'title': task.title,
            'description': task.description,
            'end_date': task.end_date
        })
    return render(request, 'task_details.html', {'form': form, 'task': task})

def delete_task(request, pk):
    if request.method == 'POST':
        Task.objects.filter(pk = pk).delete()
        return redirect('todo_list:main_page')


