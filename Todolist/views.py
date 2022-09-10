

from datetime import datetime
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import TODO


# Create your views here.
def TodO(request):
    if request.method=='POST':
        title=request.POST.get('textitle')
        list=TODO(text=title)  
        list.save()  
        
    todlist=TODO.objects.all()
    context={
        'todolists':todlist
    }
    return render(request,'todo.html',context)

def Delete(request,id):

    Tod_list=TODO.objects.get(id=id)
    Tod_list.delete()
    todlist=TODO.objects.all()
    context={
        'todolists':todlist
    }
    return redirect ('/',context)


def Edit(request,id):
        todlist=TODO.objects.get(id=id)
        context={
        'todolists':todlist
                   }
        return render (request,'edit.html',context)
  
    
def Update(request,id):
    todo_list=TODO.objects.get(id=id)
    todo_list.text=request.POST['textitle']
    todo_list.save()
    return redirect ('/')
