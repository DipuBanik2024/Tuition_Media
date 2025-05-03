from django.shortcuts import render
from .models import *


# Create your views here.
def course_detail(request):
    return render(request, template_name='courses\course_detail.html')


def course_list(request):
    return render(request, template_name='courses\course_list.html')


def lecture_notes(request):
    return render(request, template_name='courses\lecture_notes.html')


def skill_development_view(request):
    videos = SkillVideo.objects.all()
    return render(request, 'courses/skill_development.html', {'videos': videos})


def ssc_hsc_academic_programs(request):
    videos = AcademicProgramVideo.objects.all()
    return render(request, 'courses/ssc_hsc_academic_programs.html', {'videos': videos})


def admission_programs(request):
    videos = AdmissionProgram.objects.all()
    return render(request, 'courses/admission_programs.html', {'videos': videos})

