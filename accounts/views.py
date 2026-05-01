from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import register_user, login_user


# 🔹 SIGNUP API
@api_view(['POST'])
def signup(request):

    try:
        user = register_user(request.data)

        return Response({
            "message": "User registered successfully",
            "username": user.username
        })

    except Exception as e:
        return Response({"error": str(e)}, status=400)


# 🔹 LOGIN API
@api_view(['POST'])
def login(request):

    try:
        result = login_user(request.data)

        return Response({
            "message": "Login successful",
            **result
        })

    except Exception as e:
        return Response({"error": str(e)}, status=400)

from django.shortcuts import render

def login_page(request):
    return render(request, 'login.html')

def signup_page(request):
    return render(request, 'signup.html')

def dashboard_page(request):
    return render(request, 'dashboard.html')
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_users(request):

    users = User.objects.all()

    data = []
    for u in users:
        data.append({
            "id": u.id,
            "username": u.username
        })

    return Response(data)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
    return Response({
        "id":int( request.user.id),
        "username": request.user.username,
        "role": request.user.profile.role  # ✅ ADD THIS

    })