from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Custom User Manager
class UserManager(BaseUserManager):
    def create_user(self, email, phone, password=None, **extra_fields):
        if not email and not phone:
            raise ValueError('Users must have an email or phone number')
        email = self.normalize_email(email)
        user = self.model(email=email, phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, phone, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ('Tutor', 'Tutor'),
        ('Student', 'Student'),
    )
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, null=True, blank=True)
    phone = models.CharField(max_length=15, unique=True, null=True, blank=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    district = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    preferred_area = models.CharField(max_length=100, blank=True)

    profile_picture = models.ImageField(upload_to='profile_pictures/',default='images/defaultprofile.png',blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']


    def __str__(self):
        return self.name

class Qualification(models.Model):
    DEGREE_CHOICES = [
        ('SSC', 'SSC'),
        ('HSC', 'HSC'),
        ('BSc', 'BSc'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='qualifications')
    degree = models.CharField(max_length=50, choices=DEGREE_CHOICES)
    result = models.CharField(max_length=20)
    year = models.CharField(max_length=4)
    institute = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.degree} - {self.user.name}'
