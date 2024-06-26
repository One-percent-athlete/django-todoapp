from django.db import models
from django.contrib.auth.models import User
from datetime import date

# class User(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
    
#     last_updated = models.DateTimeField(User, auto_now=True)

#     def __str__(self):
#         return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'categories'

class Priority(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'priority'


class Todo(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    task_name = models.CharField("Task Name", max_length=50)
    task_body = models.CharField("Task Body", max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE, default=3)
    deadline = models.DateTimeField("Deadline")
    created_at = models.DateTimeField("Created At", auto_now_add=True)
    completed = models.BooleanField("Completed", default=False)

    
    def __str__(self):
        return (
            f"{self.user}"
            f"({self.created_at:%Y-%m-%d %H:%M}): "
            f"{self.task_name}..."
        )
    