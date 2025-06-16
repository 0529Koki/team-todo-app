from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo, Member

def index(request):
    todos = Todo.objects.all()
    members = Member.objects.all()
    return render(request, 'todo/base.html', {
        'todos': todos,
        'members': members
    })

def edit(request):
    return render(request, 'todo/detail.html')

def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        due_date = request.POST.get('due_date')
        assignee_id = request.POST.get('assignee')

        assignee = get_object_or_404(Member, pk=assignee_id)
        todo = Todo(title=title, due_date=due_date, assignee=assignee)
        todo.save()
        return redirect('todo:index')
    return redirect('todo:index')

def toggle_task(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todo:index')


def edit_task(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    members = Member.objects.all()

    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.due_date = request.POST.get('due_date')
        assignee_id = request.POST.get('assignee')
        todo.assignee = get_object_or_404(Member, pk=assignee_id)
        todo.save()
        return redirect('todo:index')

    return render(request, 'todo/detail.html', {
        'todo': todo,
        'members': members
    })


def delete_task(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect('todo:index')