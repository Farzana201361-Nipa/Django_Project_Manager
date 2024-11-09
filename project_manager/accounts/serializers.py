
from rest_framework import serializers
from . models import User, Projects, ProjectMembers, Tasks, Comments

#Serializers for each model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'date_joined']
    
class ProjectsSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only = True)
    class Meta:
        model = Projects
        fields = ['id', 'name', 'description', 'owner', 'created_at']
        
        
class ProjectMemberSerializer(serializers.ModelSerializer):
    project = ProjectsSerializer(read_only = True)
    user = UserSerializer(read_only = True)
    class Meta:
        model = ProjectMembers
        fields = ['id', 'project', 'user', 'role']
        
class TasksSerializer(serializers.ModelSerializer):
    assigned_to = UserSerializer(read_only = True)
    project = ProjectsSerializer(read_only = True)
    
    class Meta:
        model = Tasks
        fields = ['id', 'title', 'description', 'status','priority', 'assigned_to', 'project','created_at', 'due_date' ]
        
        
class CommentsSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)
    task =  TasksSerializer(read_only = True)
    class Meta:
        model = Comments
        fields = ['id', 'content', 'user', 'task', 'created_at']
        
        
        
        
        
        
