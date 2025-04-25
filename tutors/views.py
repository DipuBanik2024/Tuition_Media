
from django.shortcuts import render
from students.models import tutor_request_post
# Create your views here.

def find_tuitions(request):
    posts = tutor_request_post.objects.all().order_by('-timestamp')
    context= {'posts':posts}
    return render(request,template_name='tutors/find_tuitions.html',context=context)

def tuition_post(request):
    return render(request,template_name='tutors/tuition_post.html')