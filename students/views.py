from django.shortcuts import render

# Create your views here.
def tutor_list(request):
    return render(request,template_name='students/tutor_list.html')

def tutor_request(request):
    return render (request,template_name='students/tutor_request.html')