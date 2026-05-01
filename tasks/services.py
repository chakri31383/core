from .models import Task
from projects.models import Project
from django.contrib.auth.models import User


# 🔹 Create Task
def create_task(data, user):

    project = Project.objects.get(id=data['project_id'])

    # only project owner can assign task
    if project.owner != user:
        raise Exception("Only project owner can assign tasks")

    assigned_user = User.objects.get(id=data['assigned_to'])

    # ensure user is part of project
    if assigned_user not in project.members.all():
        raise Exception("User is not part of this project")

    task = Task.objects.create(
        title=data['title'],
        description=data['description'],
        project=project,
        assigned_to=assigned_user,
        deadline=data['deadline']
    )

    return task


# 🔹 Update Task Status
def update_task_status(task_id, status, user):

    task = Task.objects.get(id=task_id)

    # only assigned user can update
    if task.assigned_to != user:
        raise Exception("You can only update your own tasks")

    task.status = status
    task.save()

    return task
from datetime import date
from .models import Task

def get_dashboard_data(user):

    tasks = Task.objects.filter(assigned_to=user)

    total = tasks.count()
    completed = tasks.filter(status='DONE').count()
    pending = tasks.exclude(status='DONE').count()
    overdue = tasks.filter(deadline__lt=date.today()).exclude(status='DONE').count()

    return {
        "total_tasks": total,
        "completed": completed,
        "pending": pending,
        "overdue": overdue
    }