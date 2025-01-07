from django.db import models
from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='Pending')
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks", null=True, blank=True)
    completed_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.assigned_to}..{self.title} ({self.status})"


@receiver(post_save, sender=User)
def creat_token(sender, instance, created, *args, **kwargs):
    if created:
        Token.objects.create(user=instance)