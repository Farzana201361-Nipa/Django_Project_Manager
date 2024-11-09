from rest_framework import viewsets
from . models import User, Projects, ProjectMembers, Tasks, Comments
from . serializers import UserSerializer, ProjectsSerializer, ProjectMemberSerializer, TasksSerializer, CommentsSerializer
from rest_framework.permissions import IsAuthenticated


#Creating viewsets here

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    permission_classes = [IsAuthenticated]
    
class ProjectMembersViewSet(viewsets.ModelViewSet):
    queryset = ProjectMembers.objects.all()
    serializer_class = ProjectMemberSerializer
    permission_classes = [IsAuthenticated]
    
    
class TasksViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    permission_classes = [IsAuthenticated]
    
class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthenticated]
