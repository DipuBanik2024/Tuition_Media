"""
URL configuration for Tuition_Media project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import settings
from django.conf.urls.static import static

from main import views as main_view
from accounts import views as account_view
from courses import views as course_view
from helpline import views as helpline_view
from students import views as students_view
from tutors import views as tutors_view


urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    # main
    path('',main_view.home,name='home'),
    path('contact_us/',main_view.contact_us,name='contact_us'),
    path('about/',main_view.About,name='about'),
    # Account
    path('login/',account_view.login,name='login'),
    path('register/', account_view.register, name='register'),
    path('profile/', account_view.profile, name='profile'),
    # courses
    path('course_detail/', course_view.course_detail, name='course_detail'),
    path('course_list/', course_view.course_list, name='course_list'),
    path('lecture_notes/', course_view.lecture_notes, name='lecture_notes'),
    path('skill_development/', course_view.skill_development, name='skill_development'),
    path ('ssc_hsc_academic_programs/',course_view.ssc_hsc_academic_programs,name='ssc_hsc_academic_programs'),
    path ('admission_programs/',course_view.admission_programs,name='admission_programs'),
    # students
    path('tutor_list/', students_view.tutor_list, name='tutor_list'),
    path('tutor_request/', students_view.tutor_request, name='tutor_request'),
    # tutors
    path('find_tuitions/',tutors_view.find_tuitions, name='find_tuitions'),
    path('tuition_post/', tutors_view.tuition_post, name='tuition_post'),
    path('update/<str:id>',tutors_view.update, name='update'),
    path('delete/<str:id>', tutors_view.delete, name='delete'),
    # helpline
    path ('help_center/',helpline_view.help_center,name='help_center'),
    path ('privacy_policy/',helpline_view.privacy_policy,name='privacy_policy'),
    path ('services/',helpline_view.services,name='services'),
    path ('terms/',helpline_view.terms,name='terms'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

