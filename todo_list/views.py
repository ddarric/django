from django.shortcuts import render
from todo_list.models import Task
# Create your views here.


def main_page(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'main_page.html', context)