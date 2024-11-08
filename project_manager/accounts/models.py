from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class User(AbstractUser):
    #id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    def __str__(self):
        return self.username
    

class Projects(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owneed_projects')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class ProjectMembers(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='project_members')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='members')
    role = models.CharField(max_length=50, choices=[('Admin', 'Admin'), ('Member', 'Member')])
    
    def __str__(self):
        return f"{self.user.username} - {self.role} in {self.project.name}"
                              