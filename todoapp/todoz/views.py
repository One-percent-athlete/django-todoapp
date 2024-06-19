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
                todos = Todo.objects.filter(user__id=request.user.id) 
                return render(request, "home.html", {"todos": todos})
            else:
                messages.success(request, "You Have To Login Or Sign Up First.")
                return redirect(request, "add_todo.html", {"form":form})
        else:
            form = TodoForm()
            return render(request, "add_todo.html", {"form":form})
    else:
        messages.success(request, "You Have To Login Or Sign Up First.")
        return render(request, "home.html", )


    # if request.user.authenticated:
    #     if request.method == "POST":

    #         todos = Todo.objects.filter(user__id=request.user.id) 
    #         return render(request, "home.html", {"todos": todos})
    #     return render(request, "add_todo.html", )
    # else:
    #     return render(request, "home.html")
