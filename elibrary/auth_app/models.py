from django.db import models

class User(models.Model):
    USER_TYPES = [
        ('student', 'Student'),
        ('faculty', 'Faculty'),
        ('staff', 'Staff'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=50)
    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    password = models.CharField(max_length=255)  # Store hashed password

    # Fields specific to each user type
    student_id = models.CharField(max_length=50, blank=True, null=True)
    teacher_id = models.CharField(max_length=50, blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)  # For staff login

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.user_type})"
