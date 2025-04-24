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
    student_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    medium = models.CharField(max_length=20, choices=MEDIUM_CHOICES)
    student_class = models.CharField(max_length=30, choices=CLASS_CHOICES)
    district = models.CharField(max_length=100,blank=True,null=True)
    area = models.CharField(max_length=100 ,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.student_name} ({self.student_class}) - {self.district}"