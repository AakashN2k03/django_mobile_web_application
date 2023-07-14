from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
from django.core.mail import send_mail



# Create your views here.

def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        new_user = User.objects.create_user(username,email,password)
        new_user.save()
        if new_user is not None:
            login(request, new_user)
            return redirect('content')
        else:
            return render(request,'subprogram/login_view.html',{"username":username})
        
    
    return render(request, 'subprogram/home.html')

def login_view(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        passwords = request.POST.get('password')

        user = authenticate(request, username=name, password=passwords)
        if user is not None:
            login(request, user)
            return redirect('content')
        else:
            return HttpResponse('Error, user does not exist')
        


    return render(request, 'subprogram/login_view.html')

def content(request):
    items=category.objects.filter(status=0)
    subproduct=products.objects.filter(trending=0)
    t=tren.objects.filter(status=0)
    return render(request,'subprogram/content.html',{"items":items,"subproduct":subproduct,"t":t})

def search(request):
    if request.method=='POST':
        query=request.POST['query']
        obj=iphone.objects.filter(name__contains=query)
        obj1=redmi.objects.filter(name__contains=query)
        obj2=vivo.objects.filter(name__contains=query)
        obj3=samsung.objects.filter(name__contains=query)
        obj4=oneplus.objects.filter(name__contains=query)
        con={"obj":obj,"obj1":obj1,"obj2":obj2,"obj3":obj3,"obj4":obj4
             }
        
        return render(request,'subprogram/search.html',con)
    else:
         return render(request,'subprogram/content.html')
   

def collection1(request):
    col1=iphone.objects.filter(status=0)
    return render(request,'subprogram/collection1.html',{"col1":col1})

def collection2(request):
    col1=vivo.objects.filter(status=0)
    return render(request,'subprogram/collection2.html',{"col1":col1})

def collection3(request):
    col1=samsung.objects.filter(status=0)
    return render(request,'subprogram/collection3.html',{"col1":col1})


def collection4(request):
    col1=oneplus.objects.filter(status=0)
    return render(request,'subprogram/collection4.html',{"col1":col1})


def collection5(request):
    col1=redmi.objects.filter(status=0)
    return render(request,'subprogram/collection5.html',{"col1":col1})

def logindup(request):
     if request.method == 'POST':
        name = request.POST.get('username')
        passwords = request.POST.get('password')

        user = authenticate(request, username=name, password=passwords)
        if user is not None:
            login(request, user)
            return redirect('content')
        else:
            return HttpResponse('Error, user does not exist')
        


     return render(request, 'subprogram/login_view.html')


def logout(request):
     logout(request)
     return redirect('home')

def payment(request):
    return render(request,"subprogram/payment.html")

def tq(request):
    if request.method == "POST":
        email = request.POST.get('email')
        name = request.POST.get('name')
        feedback = request.POST.get('feedback')

        users = User.objects.filter(email=email)

        if users.exists():
            message = f'Name: {name}\nFeedback: {feedback}'
            send_mail(
                subject='Feedback',
                message=message,
                from_email=email,
                recipient_list=['aakofficial007@gmail.com'],
                fail_silently=False
            )
            return render(request, "subprogram/content.html")

    return render(request, "subprogram/tq.html")

        

       

        
  
       
  
       
    
