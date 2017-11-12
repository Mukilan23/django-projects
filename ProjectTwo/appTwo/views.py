from django.shortcuts import render
from django.http import HttpResponse
from appTwo.models import User
from appTwo.forms import NewUserForm
# Create your views here.



def index(request):
    return HttpResponse("<em>Hey There! This is my experimental project where I used to practice my django commands</em>")


def help(request):
    helpdict={'help_insert':"Help Page!"}
    return render(request,'appTwo/help.html',context=helpdict)

def users(request):
    form = NewUserForm

    if request.method == 'POST':
          form=NewUserForm(request.POST)

          if form.is_valid():
              form.save(commit=True)
              return index(request)

          else:
              print("Error")
    return render(request,"appTwo/users.html",{'form':form})
