from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .services import create_task, update_task_status
from .models import Task


# 🔹 Create Task
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_task_view(request):

    try:
        task = create_task(request.data, request.user)

        return Response({
            "message": "Task created",
            "task_id": task.id
        })

    except Exception as e:
        return Response({"error": str(e)}, status=400)


# 🔹 Update Status
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_task_view(request, task_id):

    try:
        status = request.data.get('status')

        task = update_task_status(task_id, status, request.user)

        return Response({
            "message": "Task updated",
            "status": task.status
        })

    except Exception as e:
        return Response({"error": str(e)}, status=400)


# 🔹 Get My Tasks
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_tasks(request):

    user = request.user

    # 🔥 ADMIN → see all tasks
    if user.profile.role == 'ADMIN':
        tasks = Task.objects.all()
    else:
        # MEMBER → only assigned tasks
        tasks = Task.objects.filter(assigned_to=user)

    data = []

    for t in tasks:
        data.append({
            "id": t.id,
            "title": t.title,
            "status": t.status,
            "project": t.project.name,
            "deadline": t.deadline,
            "assigned_to": t.assigned_to.username,
            "description": t.description
            # 👈 ADD THIS
        })

    return Response(data)

from .services import get_dashboard_data

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard_view(request):

    data = get_dashboard_data(request.user)

    return Response(data)
from django.shortcuts import render

def tasks_page(request):
    return render(request, 'tasks.html')