from django.shortcuts import render
from django.utils import timezone
from .models import Todo

def todo_list(request):
    todos = Todo.objects.order_by('deadline')
    context = {'todos': todos}
    return render(request, 'todolistapp/todo_list.html', context)

# Create your views here.
