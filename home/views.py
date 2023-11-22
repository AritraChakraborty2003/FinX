from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout as logouts
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request,"index.html")
def signupConsumer(request):
      if request.method=="POST":
        uname=request.POST.get("uname")
        email=request.POST.get("email")
        password=request.POST.get("password")
        user=User.objects.create_user(uname,email,password)
        user.save()
        return redirect("/")
    
      return render(request,"signupConsumer.html")
def dashboard(request):
    return render(request,"dashboard.html")
def loginConsumer(request):
    if request.method=="POST":
        uname=request.POST.get("uname")
        password=request.POST.get("password")
        user=authenticate(request,username=uname,password=password)
        if user is not None:
            login(request,user)
            return redirect("/dashboard")
        else:
            return HttpResponse("Invalid username or password")
    return render(request,"loginConsumer.html")
    
def payment(request):
    return render(request,"payment.html")
def Loan(request):
    return render(request,"LoanApproval.html")
def logout(request):
     logouts(request)
     return redirect("/")