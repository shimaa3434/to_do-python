from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import *
from .forms import *

# Create your views here.
def list (request):
    lists= get_list_or_404(ToDo)
    if request.method== 'POST':
        form= ToDoForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo:list')
    else:
        form= ToDoForms()
    if request.method == 'POST':
        check= request.POST['todo_id']
        todo= get_object_or_404(ToDo, id= check)
        if todo.checked:
            todo.checked= False
            todo.save()
        else:
            todo.checked= True
            todo.save()
    return render(request, 'todo/home.html', {'lists': lists, 'form': form})


def edit(request, pk):
    id= get_object_or_404(ToDo, pk= pk)
    form= ToDoForms(instance=id)
    if request.method== 'GET':
        form= ToDoForms(instance=id)
    else:
        form= ToDoForms(request.POST, instance=id)
        if form.is_valid():
            form.save()
            return redirect('todo:list')
    return render(request, 'todo/edit.html', {'form': form})

def delete(request, pk):
    id = get_object_or_404(ToDo, pk=pk)
    id.delete()
    return redirect('todo:list')

