from django.shortcuts import render,redirect,get_object_or_404
from .models import *

# Create your views here.
def home(request):
    value=todos.objects.all()
    context={"values":value}
    if request.method == "POST":
        data=request.POST.get
        title=data('title')
        description=data("description")
        todos.objects.create(title=title,description=description)
        return redirect('/todo/')
        
    return render(request,'index.html',context)


# delete todos
def delete_todo(request,delete_id):
    get_object_or_404(todos,id=delete_id).delete()

    return redirect("/todo/")


# update todos
def update_todo(request,update_id):
    value=get_object_or_404(todos,id=update_id)
    if request.method == "POST":
        data=request.POST.get
        title=data('title')
        description=data("description")
        value.title=title
        value.description=description
        value.save()
        return redirect('/todo')
    context={"values":value}
    return render(request,'update.html',context)
   