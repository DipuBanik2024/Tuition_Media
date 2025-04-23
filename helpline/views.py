from django.shortcuts import render

# Create your views here.
def help_center(request):
    return render (request,template_name='helpline/help_center.html')

def privacy_policy(request):
    return render (request,template_name='helpline/privacy_policy.html')

def services(request):
    return render (request,template_name='helpline/services.html')

def terms(request):
    return render (request,template_name='helpline/terms.html')
