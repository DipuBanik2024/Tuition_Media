from django.contrib import admin
from .models import SkillVideo
from .models import AcademicProgramVideo
from .models import AdmissionProgram



# Register your models here.
admin.site.register(SkillVideo)
admin.site.register(AcademicProgramVideo)
admin.site.register(AdmissionProgram)
