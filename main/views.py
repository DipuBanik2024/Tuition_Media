from django.shortcuts import render,redirect
from .forms import ContactForm
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,template_name='main\home.html')

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, message='Your message has been sent successfully!')
            return redirect('contact_us')
    else:
        form = ContactForm()
    return render(request, template_name='main\contact_us.html', context={'form': form})

def About(request):
    return render(request,template_name='main\About.html')

