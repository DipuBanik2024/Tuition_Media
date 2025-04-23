from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
# courses/models.py


User = get_user_model()

class Course(models.Model):
    COURSE_TYPE_CHOICES = [
        ('Academic', 'Academic'),
        ('Skill', 'Skill Devolopment'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    course_type = models.CharField(max_length=50, choices=COURSE_TYPE_CHOICES)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses')
    pdf_file = models.FileField(upload_to='courses/pdfs/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.course_type})"
