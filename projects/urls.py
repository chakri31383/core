from django.urls import path
from .views import create_project_view, add_members_view, my_projects,project_members

urlpatterns = [
    path('create/', create_project_view),
    path('<int:project_id>/add-members/', add_members_view),
    path('my/', my_projects),
    path('<int:project_id>/members/', project_members),
]