from django.shortcuts import render, redirect
from students.models import tutor_request_post
from students.forms import TutorRequestForm  # Assuming this is the form for the post
from .forms import TutorPostForm
from .models import Tutor
# View: Show all tuition posts (for tutors to browse)
def find_tuitions(request):
    posts = tutor_request_post.objects.all().order_by('-timestamp')
    context = {'posts': posts}
    return render(request, 'tutors/find_tuitions.html', context)

# View: Update tuition post
def update(request, id):
    posts = tutor_request_post.objects.get(pk=id)
    form = TutorRequestForm(instance=posts)
    if request.method == 'POST':
        form = TutorRequestForm(request.POST, instance=posts)
        if form.is_valid():
            form.save()
            return redirect('find_tuitions')
    context = {'form': form}
    return render(request, 'tutors/update.html', context)

# View: Delete tuition post
def delete(request, id):
    posts = tutor_request_post.objects.get(pk=id)
    if request.method == 'POST':
        posts.delete()
        return redirect('find_tuitions')
    return render(request, 'tutors/delete.html')

# ✅ Updated View: Create a new tuition post

def tuition_post(request):
    if request.method == 'POST':
        form = TutorPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tutor_list')  # Redirect to student app's tutor list
    else:
        form = TutorPostForm()
    return render(request, 'tutors/tuition_post.html', {'form': form})
