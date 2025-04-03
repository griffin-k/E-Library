# models.py
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

class Student(AbstractBaseUser):
    DEPARTMENT_CHOICES = (
        ('BSCS', 'BSCS'),
        ('BSIT', 'BSIT'),
        ('BSSE', 'BSSE'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    student_id = models.CharField(max_length=20, unique=True)
    cell_no = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=10, choices=DEPARTMENT_CHOICES)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'student_id', 'cell_no', 'department']

    def __str__(self):
        return f"{self.first_name} {self.last_name} (Student)"

class Faculty(AbstractBaseUser):
    DEPARTMENT_CHOICES = (
        ('BSCS', 'BSCS'),
        ('BSIT', 'BSIT'),
        ('BSSE', 'BSSE'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    faculty_id = models.CharField(max_length=20, unique=True)
    cell_no = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=10, choices=DEPARTMENT_CHOICES)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'faculty_id', 'cell_no', 'department']

    def __str__(self):
        return f"{self.first_name} {self.last_name} (Faculty)"

class Staff(AbstractBaseUser):
    DEPARTMENT_CHOICES = (
        ('BSCS', 'BSCS'),
        ('BSIT', 'BSIT'),
        ('BSSE', 'BSSE'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    staff_id = models.CharField(max_length=20, unique=True)
    cell_no = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=10, choices=DEPARTMENT_CHOICES)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'staff_id', 'cell_no', 'department']

    def __str__(self):
        return f"{self.first_name} {self.last_name} (Staff)"