from django.db import models

# Create your models here.

class Task(models.Model):

    STATUS_CHOICES = (
        ('To Do', 'To Do'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed')
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='To Do')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title