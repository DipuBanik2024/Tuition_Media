from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,template_name='main\home.html')

def contact_us(request):
    return render(request,template_name='main\contact_us.html')

def About(request):
    return render(request,template_name='main\About.html')

