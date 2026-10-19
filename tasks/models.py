from django.db import models

# Create your models here.
class Task(models.Model):
    PRIORITY_TYPES = [
        ('low','Low'),
        ('medium','Medium'),
        ('high','High'),
    ]

    title  = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    is_completed = models.BooleanField()
    priority = models.CharField(max_length=100, choices=PRIORITY_TYPES, default='medium')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return {self.title}