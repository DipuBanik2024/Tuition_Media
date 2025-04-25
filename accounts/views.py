from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,template_name='accounts\login.html')

def register(request):
    return render(request,template_name='accounts/register.html')

def profile(request):
    return render(request,template_name='accounts\profile.html')