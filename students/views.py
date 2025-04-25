from django.shortcuts import render, redirect
from .models import *
from .forms import *

def tutor_request(request):
    form = TutorRequestForm()
    if request.method == 'POST':
        form = TutorRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('find_tuitions')  # or wherever you want to redirect
    context={'form':form}
    return render(request,template_name='students/tutor_request.html',context=context)


def tutor_list(request):
    return render(request,template_name='students/tutor_list.html')

