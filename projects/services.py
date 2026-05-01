from .models import Project
from django.contrib.auth.models import User

# 🔹 Create Project
def create_project(data, user):

    # only admin can create
    if user.profile.role != 'ADMIN':
        raise Exception("Only admin can create project")

    project = Project.objects.create(
        name=data['name'],
        description=data['description'],
        owner=user
    )

    # add owner automatically as member
    project.members.add(user)

    return project


# 🔹 Add Members
def add_members(project_id, member_ids, user):

    project = Project.objects.get(id=project_id)

    # only owner can add members
    if project.owner != user:
        raise Exception("Only owner can add members")

    for uid in member_ids:
        member = User.objects.get(id=uid)
        project.members.add(member)

    return project