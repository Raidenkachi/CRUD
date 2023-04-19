from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseNotFound
from myapp.models import Student,Employee
from myapp.forms import StudentForm


def image(request):
    return render(request,'images.html')
def hello(request):
    return HttpResponse("Hello welcome to Django")
def background(request):
   return render(request,'background.html')

def members(request):
    all = Student.objects.all()
    return render(request, 'members.html', {'members':all})

def student(request):
   if request.method=='post':
       form=StudentForm(request.post)
       if form.is_valid():
           form.save()
           return redirect("/")
   else:
       form=StudentForm()
       return render(request, 'student.html',{'form':form})


def sacarstic(request):
    emp= EmployeeForm()
    return render(request, 'sacarsm.html', {'form':emp})

def setsession(request):
    request.session['firstname']='Zeus'
    request.session['lastname']='Kratos'
    request.session['email']='collinsopindi@gmail.com'
    return HttpResponse("Session has been successfully created")


def getsession(request):
    fname=request.session['firstname']
    lname=request.session['lastname']
    email=request.session['email']
    return HttpResponse(fname + ' '+ lname + ' ' + email)

def animal(request):
    return render(request, 'forms.html')


# Create your views here.
