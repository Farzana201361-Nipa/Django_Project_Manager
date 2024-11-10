from rest_framework import viewsets, status, permissions
from . models import User, Projects, ProjectMembers, Tasks, Comments
from . serializers import UserSerializer, ProjectsSerializer, ProjectMemberSerializer, TasksSerializer, CommentsSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView


#Creating viewsets here

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = [IsAuthenticated]
    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def login(self, request):
        return TokenObtainPairView.as_view()(request._request)
    
    
    @action(detail=True, methods=['get'], permission_classes=[IsAuthenticated])
    def details(self, request, pk=None):
        user = self.get_object()
        serializer = self.get_serializer(user)
        return Response(serializer.data)
    
    @action(detail=True, methods=['put', 'patch'], permission_classes=[IsAuthenticated])
    def update_user(self, request, pk=None):
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['delete'], permission_classes=[IsAuthenticated])
    def delete_user(self, request, pk=None):
        user = self.get_object()
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
    
class IsProjectOwner(permissions.BasePermission):
    #Only owner can edit or delete
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user   
    
class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    permission_classes = [IsAuthenticated]


    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsProjectOwner]  
        else:
            self.permission_classes = [permissions.IsAuthenticated]  
        return super().get_permissions()
    

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user) 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):

        project = self.get_object()
        serializer = self.get_serializer(project)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        project = self.get_object()
        self.check_object_permissions(request, project)  
        serializer = self.get_serializer(project, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        project = self.get_object()
        self.check_object_permissions(request, project) 
        serializer = self.get_serializer(project, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        project = self.get_object()
        self.check_object_permissions(request, project) 
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
class ProjectMembersViewSet(viewsets.ModelViewSet):
    queryset = ProjectMembers.objects.all()
    serializer_class = ProjectMemberSerializer
    permission_classes = [IsAuthenticated]
    
   
class TasksViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()  
    serializer_class = TasksSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        project_id = self.kwargs.get('project_id')  
        if project_id:
            return Tasks.objects.filter(project_id=project_id)  
        return super().get_queryset()
    
    def create(self, request, *args, **kwargs):
        project_id = self.kwargs.get('project_id')
        if not project_id:
            return Response({"error": "Project ID is required."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            project = Projects.objects.get(id=project_id)
        except Projects.DoesNotExist:
            return Response({"error": "Project not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(project=project)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)  
    
class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthenticated]
    
    
    
