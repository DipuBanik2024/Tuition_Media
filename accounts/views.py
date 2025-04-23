from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,template_name='accounts\login.html')

def Register(request):
    return render(request,template_name='accounts\Register.html')

def profile(request):
    return render(request,template_name='accounts\profile.html')