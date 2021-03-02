from django.shortcuts import render
from django.http import HttpResponse
from .models import TodoApp

# Create your views here.
def home(request):
    allTodoData=TodoApp.objects.all().order_by("-id")
    return render(request,"index.html",{"data":allTodoData})
   