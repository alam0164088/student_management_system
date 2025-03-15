from django.db import models

class Student(models.Model):
    DEPARTMENT_CHOICES = (
        ('CSE', 'Computer Science & Engineering'),
        ('EEE', 'Electrical & Electronic Engineering'),
        ('CIVIL', 'Civil Engineering'),
        ('ME', 'Mechanical Engineering'),
    )
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    course = models.CharField(max_length=100)
    department = models.CharField(max_length=10, choices=DEPARTMENT_CHOICES)  # default মুছে দিয়েছি

    def __str__(self):
        return f"{self.name} ({self.department})"

class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.code} - {self.name}"