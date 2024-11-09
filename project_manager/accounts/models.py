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
    role = models.CharField(max_length=50, choices=[('Admin', 'Admin'), 
                                                    ('Member', 'Member')])
    
    def __str__(self):
        return f"{self.user.username} - {self.role} in {self.project.name}"
    
 
 
class Tasks(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=50, 
                              choices=[ ('To Do', 'To Do'),
                                        ('In Progress','In Progress'),
                                        ('Done', 'Done')])
    priority = models.CharField(max_length=50, 
                              choices=[ ('Low', 'Low'),
                                        ('Medium','Medium'),
                                        ('High', 'High')])
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,null=True,blank=True, related_name='assigned_tasks')
    
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()

    
    def __str__(self):
        return f"{self.title} - {self.status} - Priority: {self.priority}"  
    
    
    
class Comments(models.Model):
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Commented by: {self.user.username} on {self.task.title}" 
    
    
    
    

                              