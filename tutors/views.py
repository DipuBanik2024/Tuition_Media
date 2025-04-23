from django.shortcuts import render

# Create your views here.
def find_tuitions(request):
    return render(request,template_name='tutors/find_tuitions.html')