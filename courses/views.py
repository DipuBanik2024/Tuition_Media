from django.shortcuts import render
from .models import *
# Create your views here.
def course_detail(request):
    courses = Course.objects.all()
    context={
        'courses':courses
    }
    return render(request,template_name='courses\course_detail.html',context=context)

def course_list(request):
    return render(request,template_name='courses\course_list.html')

def lecture_notes(request):
    return render(request,template_name='courses\lecture_notes.html')

def skill_development(request):
    return render(request,template_name='courses\skill_development.html')

def ssc_hsc_academic_programs(request):
    return render(request, template_name='courses/ssc_hsc_academic_programs.html')

def admission_programs(request):
    return render(request,template_name='courses/admission_programs.html ')

