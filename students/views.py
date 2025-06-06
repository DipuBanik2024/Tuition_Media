from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from .forms import *
from tutors.models import *
from tutors.forms import *
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
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
    tutors = Tutor.objects.all().order_by('-timestamp')

    # Get filter parameters from GET request
    location = request.GET.get('location')
    fee = request.GET.get('tuition_fee')
    subject = request.GET.get('subjects')

    # Apply filters if they exist
    if location:
        tutors = tutors.filter(location__icontains=location)
    if fee:
        try:
            fee = float(fee)
            tutors = tutors.filter(tuition_fee__lte=fee)
        except ValueError:
            pass  # ignore invalid fee input
    if subject:
        tutors = tutors.filter(subjects__icontains=subject)

    return render(request, 'students/tutor_list.html', {'tutors': tutors})

def updateT(request, id):
    posts = Tutor.objects.get(pk=id)
    form = TutorPostForm(instance=posts)
    if request.method == 'POST':
        form = TutorPostForm(request.POST,request.FILES, instance=posts)
        if form.is_valid():
            form.save()
            return redirect('tutor_list')
    context = {'form': form}
    return render(request, 'students/updateT.html', context)


def deleteT(request, id):
        posts = Tutor.objects.get(pk=id)
        if request.method == 'POST':
            posts.delete()
            return redirect('tutor_list')
        return render(request, template_name='students/deleteT.html')

