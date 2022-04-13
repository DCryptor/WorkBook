from django.shortcuts import render

# Create your views here.


def Index(request):
    return render(request, 'index.html')


def Disk(request):
    return render(request, 'disk.html')


def Programs(request):
    return render(request, 'programs.html')


def SignIn(request):
    return render(request, 'signin.html')


def SignUp(request):
    return render(request, 'signup.html')
