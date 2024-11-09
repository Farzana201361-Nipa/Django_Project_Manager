from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from . models import User, Projects, ProjectMembers, Tasks, Comments
from . serializers import UserSerializer, ProjectsSerializer, ProjectMemberSerializer, TasksSerializer, CommentsSerializer




# Create your views here.
def home(request):
    return HttpResponse("Hello 'accounts' app working on project management")


#Creating viewsets

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    
class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
   
    
class ProjectMembersViewSet(viewsets.ModelViewSet):
    queryset = ProjectMembers.objects.all()
    serializer_class = ProjectMemberSerializer
    
    
class TasksViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    
class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
