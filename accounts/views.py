from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, LoginForm
from .models import User

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    error = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            identifier = form.cleaned_data['identifier']
            password = form.cleaned_data['password']

            # Try to get user by email or phone
            user = None
            try:
                user = User.objects.get(email=identifier)
            except User.DoesNotExist:
                try:
                    user = User.objects.get(phone=identifier)
                except User.DoesNotExist:
                    user = None

            if user and user.check_password(password):
                login(request, user)
                return redirect('profile')
            else:
                error = 'Invalid credentials'
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form, 'error': error})

def profile_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user_profile = request.user
    return render(request, 'accounts/profile.html', {'user_profile': user_profile})

from .models import Qualification

@login_required
def edit_profile_view(request):
    user_profile = request.user  # ei line correct!

    if request.method == 'POST':
        user_profile.name = request.POST.get('name')
        user_profile.phone = request.POST.get('phone')
        user_profile.district = request.POST.get('district')
        user_profile.location = request.POST.get('location')
        user_profile.preferred_area = request.POST.get('preferred_area')

        if 'profile_picture' in request.FILES:
            user_profile.profile_picture = request.FILES['profile_picture']

        user_profile.save()

        # Clear previous qualifications
        Qualification.objects.filter(user=request.user).delete()

        # Save new qualifications
        degrees = request.POST.getlist('degree')
        results = request.POST.getlist('result')
        years = request.POST.getlist('year')
        institutes = request.POST.getlist('institute')

        for degree, result, year, institute in zip(degrees, results, years, institutes):
            if degree and result and year and institute:  # Ensure all fields filled
                Qualification.objects.create(
                    user=request.user,
                    degree=degree,
                    result=result,
                    year=year,
                    institute=institute
                )

        return redirect('profile')

    return render(request, 'accounts/edit_profile_view.html', {'user_profile': user_profile})


def logout_view(request):
    logout(request)
    return redirect('login')
