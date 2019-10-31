from django.shortcuts import render
from todo_list.models import Task
from todo_list.forms import NewTaskForm
from datetime import date
# Create your views here.


def main_page(request):
    if request.method == 'POST':
        print(request.POST)
        form = NewTaskForm(request.POST)
        if form.is_valid():
            print(type(form.cleaned_data['end_date']))
            task = Task(
                title = form.cleaned_data['title'],
                description = form.cleaned_data['description'],
                end_date = form.cleaned_data['end_date']
            )
            task.save()
            print('abc')
            #Perform database insertions
            """
            'tasks': tasks,
            'form': form,
            'title': form.cleaned_data['title'],
            'description': form.cleaned_data['description'],
            #'end_date': form.cleaned_data['end_date'] 
            """
            #Return error or ok messages
        else:
            print('toto')
    else:
        form = NewTaskForm()
    tasks = Task.objects.all()
    return render(request, 'main_page.html', {'form': form, 'tasks': tasks})

    """
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    form = NewTaskForm()
    return render(request, 'main_page.html', context)
    """