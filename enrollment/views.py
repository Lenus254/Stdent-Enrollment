from distutils.command.install_egg_info import safe_name
from email.headerregistry import Address
from django.shortcuts import render
from enrollment.forms import studentform, SForm
from .models import Student
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def show(request):
    return render(request,"home.html")

def register(request):
    title="New Student Registration"
    form=studentform(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['s_name']
        clas = form.cleaned_data['s_class']
        address = form.cleaned_data['s_address']
        faculty = form.cleaned_data['s_faculty']
        mail = form.cleaned_data['s_mail']
        
        p= Student(s_name=name, s_class=clas, s_address=address, s_faculty=faculty, s_mail=mail)
        p.save()
        return render(request,'ack.html',{"title":"registered successfully"})
        
    context={"title":title,
             "form":form
             }
    return render(request,'register.html',context)

def existing(request):
    title = "Registered Students"
    allStudents=Student.objects.all()
    
    context = {
        "title":title,
        "allStudents":allStudents,
        
    }
    return render(request,'existing.html',context)

def search(request):
    title="Search Student"
    form=SForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['s_name']
        allStudents=Student.objects.filter(s_name=name)
        context = {
             'title':title,
             "allStudents":allStudents, 
        }
        return render(request,'existing.html',context)
        
    context = {
        'title':title,
        'form':form,
    }
    return render(request,'search.html', context)


def dropout(request):
    title="Drop student"
    form=SForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['s_name']
        allStudents=Student.objects.filter(s_name=name).delete()
        
        return render(request,'ack.html',{'title':"Student Deregidtered From School Database"})
        
    context = {
        'title':title,
        'form':form,
    }
    return render(request,'drop.html', context)
        
        
        