from django.contrib.auth.models import User
from django.db import models

STATUS=(
    ('Not Started','Not Started'),
    ('In Progress','In Progress'),
    ('Completed','Completed'),
)

class Task(models.Model):
    title=models.CharField(max_length=100)
    details=models.TextField(blank=True, null=True)
    deadline=models.DateField(blank=True,null=True)
    status=models.CharField(
        max_length=30,
        choices=STATUS,
        default='Not Started',
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title