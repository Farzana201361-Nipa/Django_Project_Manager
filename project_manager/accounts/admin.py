from django.contrib import admin
from . models import Projects, ProjectMembers, Tasks, Comments


# Register your models here.
admin.site.register(Projects)
admin.site.register(ProjectMembers)
admin.site.register(Tasks)
admin.site.register(Comments)

