from django.db import models
from django.contrib.auth.models import User
from projects.models import Project

class Task(models.Model):

    STATUS_CHOICES = [
        ('TODO', 'Todo'),
        ('IN_PROGRESS', 'In Progress'),
        ('DONE', 'Done'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()

    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    assigned_to = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tasks'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='TODO'
    )

    deadline = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    def is_overdue(self):
        from datetime import date
        return self.deadline < date.today() and self.status != 'DONE'

    def __str__(self):
        return self.title