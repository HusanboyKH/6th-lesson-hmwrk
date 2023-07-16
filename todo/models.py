from django.db import models
import datetime

from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('a','Admin'),
        ('s','Student'),
        ('t','Teacher'),
        ('p','Parent')
    )
    roles =     models.CharField(max_length=1,choices=ROLE_CHOICES)

# Create your models here.

class ToDoModel(models.Model):
    task = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.datetime.now)
    updated_at = models.DateTimeField(default=datetime.datetime.now)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None, null=True)

    def str(self):
        return self.task


class Meta:
    db_table = 'todo'