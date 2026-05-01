from django.urls import path
from .views import create_task_view, update_task_view, my_tasks,dashboard_view

urlpatterns = [
    path('create/', create_task_view),
    path('<int:task_id>/update/', update_task_view),
    path('my/', my_tasks),
    path('dashboard/', dashboard_view),

]