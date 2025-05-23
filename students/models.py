from django.db import models

# Create your models here.
class tutor_request_post(models.Model):
    CLASS_CHOICES = [

        ('Class 1', 'Class 1'),
        ('Class 2', 'Class 2'),
        ('Class 3', 'Class 3'),
        ('Class 4', 'Class 4'),
        ('Class 5', 'Class 5'),
        ('Class 6', 'Class 6'),
        ('Class 7', 'Class 7'),
        ('Class 8', 'Class 8'),
        ('Class 9', 'Class 9'),
        ('Class 10', 'Class 10'),
        ('HSC 1st Year', 'HSC 1st Year'),
        ('HSC 2nd Year', 'HSC 2nd Year'),
    ]

    MEDIUM_CHOICES = [
        ('Bangla', 'Bangla'),
        ('English', 'English'),
    ]
    GENDER_CHOICES = [
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE'),
        ('MALE/FEMALE', 'MALE/FEMALE'),
    ]

    student_name = models.CharField(max_length=100)  # blank=False by default
    contact_number = models.CharField(max_length=20, blank=True, null=True)  # Optional
    medium = models.CharField(max_length=20, choices=MEDIUM_CHOICES,default='Bangla')  # Required choice
    student_class = models.CharField(max_length=30, choices=CLASS_CHOICES,default='class 10')  # Required choice
    preferred_tutor = models.CharField(max_length=20, choices=GENDER_CHOICES,default='MALE')  # Required choice
    subject = models.CharField(max_length=100, blank=True, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tutoring_days = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_name} ({self.student_class}) - {self.district}"