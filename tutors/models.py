from django.db import models

class Tutor(models.Model):

    MEDIUM_CHOICES = [
        ('Bangla', 'Bangla'),
        ('English', 'English'),
        ('Bangla/English', 'Bangla/English'),

    ]
    profile_picture = models.ImageField(upload_to='tutor_profiles/', blank=True, null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, blank=True, null=True)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    medium = models.CharField(max_length=20, choices=MEDIUM_CHOICES, default='Bangla')  # Required choice
    graduation_info = models.CharField(max_length=100, blank=True, null=True)
    institutions = models.CharField(max_length=50,blank=True, null=True)
    experience_years = models.PositiveIntegerField(default=0)
    location = models.CharField(max_length=100, blank=True, null=True)
    join_date = models.DateField(auto_now_add=True)
    tuition_fee = models.PositiveIntegerField(default=0)
    subjects = models.TextField(max_length=100,blank=True, null=True)
    short_bio = models.TextField(max_length=100,blank=True, null=True)

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
