from django.urls import path
from .views import signup, login,get_users,current_user

urlpatterns = [
    path('signup/', signup),
    path('login/', login),
    path('users/', get_users),
path('me/', current_user),
]