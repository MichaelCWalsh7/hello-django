from django.shortcuts import render  # noqa: F401


# Create your views here.
def get_todo_list(request):
    return render(request, 'todo/todo_list.html')
