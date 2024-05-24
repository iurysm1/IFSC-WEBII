from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import TodoList, Item
from .forms import CreateNewList
from django.contrib.auth.decorators import login_required

@login_required()
def list(request, id):
    ls = TodoList.objects.get(id=id)

    if request.method == 'POST':
        
        if request.POST.get("save"):
            for item in ls.item_set.all():
                if request.POST.get("c"+str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                item.save()
        elif request.POST.get("newItem"):
            text = request.POST.get("new")
            ls.item_set.create(text=text, complete=False)
        return render(request, 'main/list.html', {'ls': ls})

    return render(request, 'main/list.html', {'ls': ls})


def home(request):
    return render(request, 'main/home.html')

@login_required()
def view(request):
    return render(request, 'main/view.html', {})


def create(request):
    if request.method == 'POST':
        form = CreateNewList(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            todo = TodoList(name=name)
            todo.save()
            request.user.todolist.add(todo)
            return redirect("/%i" %todo.id)
    else:
        form = CreateNewList()
    return render(request, 'main/create.html', {"form":form})

