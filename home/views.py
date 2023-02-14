from django.shortcuts import render,redirect
#from django.http import HttpResponse
from .models import product
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth







def update(request):
    return render(request, 'updateproduct.html')

def home(request):
    return render(request, 'home.html')

def addproduct(request):
    if request.method=='POST':
        p=product()
        p.productname=request.POST['productname']
        f=request.POST['price']
        f=int(f)
        p.price=f
        p.discription=request.POST['discription']
        p.save()
        messages.success(request, "product added successfully")
        return render(request,'addproducts.html')
    else:
        return render(request,'addproducts.html')

#show product
def showproduct(request):
    data=product.objects.all()   
    return render(request,'showproducts.html',{'data':data})

#update products
def updateproduct(request):
        # p=product()
        # p.productname=request.POST['pname']
        # f=request.POST['price']
        # f=int(f)
        # p.fees=f
        # p.discription=request.POST['discrption']
        # p.save()
        # st=product.objects.all()
        # #print(st)
        return render(request,'updateproduct.html')    
# def showformdata(request):
def signup(request):
    if request.method=='POST':
        uname=request.POST['uname']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['pwd']
        rpassword=request.POST['rpwd']
        if User.objects.filter(username=uname).exists():
            messages.info(request,"username already exists")
            return redirect("/")
        elif User.objects.filter(email=email).exists():
            messages.info(request,"email already exists")
            return redirect("/")
        elif password!=rpassword:
            messages.info(request,"password missmatched")
            return redirect("/")
        else:
            user=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,password=password)
        user.save()
        messages.success(request,"signed up sucessfully")
        return redirect("/")
    else:
        return render(request,'signup.html')
def login(request):
    if request.method=='POST':
        uname=request.POST['uname']
        password=request.POST['password']
        user=auth.authenticate(username=uname,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"Invalid username or password")
            return render(request,'login.html')
    else:
        return render(request,'login.html') 
def logout(request):
    auth.logout(request)
    messages.info(request,'Logout sucessfully')
    return redirect("/")        


               


        
