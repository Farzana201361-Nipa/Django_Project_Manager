from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'accounts'

#Creating router
router = DefaultRouter()
#registering each viewsets with a route
router.register(r'users', views.UserViewSet)
router.register(r'projects', views.ProjectsViewSet)
router.register(r'project-members', views.ProjectMembersViewSet)
router.register(r'tasks', views.TasksViewSet)
router.register(r'comments', views.CommentsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
]

