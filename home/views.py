from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import authenticate,login
# Create your views here.
# password Bikram12
def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')


def loginUser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        #check if currect details
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
    # A backend authenticated the credentials
        
    
        else:
            return render(request,'login.html')
    # No backend authenticated the credentials
    return render(request,'login.html')   
    
    
def logoutUser(request):
    logout(request)
    return redirect("/login")
    return render(request,'index.html')