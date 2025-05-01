
from django.shortcuts import render, redirect
from students.models import tutor_request_post
from students.forms import *
# Create your views here.

def find_tuitions(request):
    posts = tutor_request_post.objects.all().order_by('-timestamp')
    context= {'posts':posts}
    return render(request,template_name='tutors/find_tuitions.html',context=context)

def update(request,id):
    posts= tutor_request_post.objects.get(pk=id)
    form=TutorRequestForm(instance=posts)
    if request.method=='POST':
        form = TutorRequestForm(request.POST,instance=posts)
        if form.is_valid():
            form.save()
            return redirect('find_tuitions')
    context={
        'form':form,
    }
    return render(request,template_name='tutors/update.html',context=context)

def delete(request,id):
    posts = tutor_request_post.objects.get(pk=id)
    if request.method == 'POST':
        posts.delete()
        return redirect('find_tuitions')
    return render(request,template_name='tutors/delete.html')

def tuition_post(request):
    return render(request,template_name='tutors/tuition_post.html')