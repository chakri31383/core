from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

# 🔹 SIGNUP
def register_user(data):

    # check if user exists
    if User.objects.filter(username=data['username']).exists():
        raise Exception("Username already exists")

    # create user
    user = User.objects.create_user(
        username=data['username'],
        email=data['email'],
        password=data['password']
    )

    # update profile
    profile = user.profile
    profile.full_name = data['full_name']

    # first user becomes ADMIN
    if User.objects.count() == 1:
        profile.role = 'ADMIN'
    else:
        profile.role = 'MEMBER'

    profile.save()

    return user


# 🔹 LOGIN
def login_user(data):

    user = authenticate(
        username=data.get('username'),
        password=data.get('password')
    )

    if not user:
        raise Exception("Invalid username or password")

    if not user.is_active:
        raise Exception("Account is disabled")

    refresh = RefreshToken.for_user(user)

    return {
        "access_token": str(refresh.access_token),
        "username": user.username,
        "role": user.profile.role
    }