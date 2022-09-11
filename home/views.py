from django.http import HttpRequest
from django.shortcuts import redirect, render

from home.models import Todo

# Create your views here.


def list_todo_items(request):
    todo_list = Todo.objects.all()
    return render(request, 'home/todo_list.html', {'todo_list': todo_list})


def insert_todo_item(request: HttpRequest):
    todo = Todo(content=request.POST['content'])
    todo.save()
    return redirect('/home/')


def delete_todo_item(request, todo_id):
    todo_to_delete = Todo.objects.get(id=todo_id)
    todo_to_delete.delete()
    return redirect('/home/')
