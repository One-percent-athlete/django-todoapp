from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Todo
from .forms import TodoForm

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        todos = Todo.objects.filter(user__id=request.user.id) 
        return render(request, "home.html", {"todos": todos})
    else:
        return render(request, "home.html")
    
def add_todo(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = TodoForm(request.POST)
            if form.is_valid():
                task = form.save(commit=False)
                task.user = request.user
                task.save()
            messages.success(request, "Task Added Successfully..")
            return redirect("home")
        else:
            form = TodoForm()
            return render(request, "add_todo.html", {"form":form})
    else:
        messages.success(request, "You Have To Login Or Sign Up First.")
        return render(request, "home.html", )

def edit_todo(request, pk):
    todo = Todo.objects.get(id=pk) 
    if request.user.is_authenticated:
        form = TodoForm(request.POST or None, instance=todo)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, "Your Task Has Been Updated Successfully!")
                return redirect("home")
        else:
            return render(request, "edit_todo.html", {"form": form, "todo": todo })
    else:
        messages.success(request, "Access Denied...")
        return redirect("home")
    
def delete_todo(request, pk):
    todo = Todo.objects.get(id=pk) 
    if request.user.is_authenticated:
        todo.delete()
        messages.success(request, "Task Deleted Successfully.")
        return redirect('home')
    else:
        messages.success(request, "You Are Not Authorised To Delete This Task.")
        return redirect('home')
    

def toggle_complete(request, pk):
    todo = Todo.objects.get(id=pk) 
    if request.user.is_authenticated:
        if request.method == "POST":
            status = request.POST["complete"]
            if status == "true":
                todo.completed=True
                todo.save()
            elif status == "false":
                todo.completed=False
                todo.save()
        messages.success(request, "Complete Status Updated")
        return redirect("home")
    else:
        messages.success(request, "You Are Not Authorised To Carry This Task.")
        return redirect('home')
    

    