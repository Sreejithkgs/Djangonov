from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import category,product
# for displaying all categories
def allcategories(request):
    b=category.objects.all()
    return render(request,'category.html',{'b':b})

def allproducts(request,n):
    b=category.objects.get(id=n)
    c=product.objects.filter(category=b)
    return render(request,'product.html',{'b':b,'c':c})

def showdetail(request,n):
    p=product.objects.get(id=n)
    return render(request,'detail.html',{'p':p})
def register(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        c=request.POST['c']
        e=request.POST['e']
        f=request.POST['f']
        l=request.POST['l']
        if(c==p):
          b=User.objects.create_user(username=u,password=p,email=e,first_name=f,last_name=l)
          b.save()
          return redirect('shop:category1')
        else:
            return HttpResponse("Passwords are not same")
    return render(request,'Register.html',)

def user_login(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return redirect('shop:category1')
        else:
            return HttpResponse('Invalid Credentials')

    return render(request,'login.html')
def user_logout(request):
    logout(request)
    return user_login(request)