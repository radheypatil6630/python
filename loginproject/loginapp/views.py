from django.shortcuts import render
from django.http import HttpResponse

def login_view(request):
    if request.mwthod=='POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        if username == "admin" and password == "admin":
            return HttpResponse("login done")
        else:
            return HttpResponse("login failed")
    return render(request,'loginapp/login.html')


