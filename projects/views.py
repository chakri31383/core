from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import create_project, add_members
from .models import Project
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes



# 🔹 Create Project
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_project_view(request):

    try:
        project = create_project(request.data, request.user)

        return Response({
            "message": "Project created",
            "project_id": project.id
        })

    except Exception as e:
        return Response({"error": str(e)}, status=400)


# 🔹 Add Members
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_members_view(request, project_id):

    try:
        member_ids = request.data.get('members', [])

        project = add_members(project_id, member_ids, request.user)

        return Response({
            "message": "Members added successfully"
        })

    except Exception as e:
        return Response({"error": str(e)}, status=400)


# 🔹 Get My Projects
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_projects(request):

    user = request.user
    projects = Project.objects.filter(members=user)

    data = []

    for p in projects:
        data.append({
            "id": p.id,
            "name": p.name,
            "owner_id": int(p.owner.id)   # 🔥 force int
        })

    return Response(data)
from django.shortcuts import render

def projects_page(request):
    return render(request, 'projects.html')
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Project

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def project_members(request, project_id):

    try:
        project = Project.objects.get(id=project_id)

        members = project.members.all()

        data = []
        for m in members:
            data.append({
                "id": m.id,
                "username": m.username
            })

        return Response(data)

    except Project.DoesNotExist:
        return Response({"error": "Project not found"}, status=404)