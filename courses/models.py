from django.db import models

# Create your models here.




class SkillVideo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    video_file = models.FileField(upload_to='videos/')  # file upload folder
    timestamp = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return self.title

class AcademicProgramVideo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    video_file = models.FileField(upload_to='academic_videos/')
    timestamp = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return self.title

class AdmissionProgram(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    video_file = models.FileField(upload_to='admission_videos/')
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return self.title
