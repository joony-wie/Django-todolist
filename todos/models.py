from django.db import models
from django.utils import timezone


class Todo(models.Model):
    # id = models.AutoField(primary_key=True) : Automatic primary key fields in Django
    title = models.CharField(max_length=50)
    text = models.TextField()
    deadline = models.DateTimeField(blank=True, null=True)
    priority = models.PositiveIntegerField(default=1)
    completed = models.BooleanField(default=False)

    # timestamp = models.DateField(auto_now_add=True, auto_now=False)
    def is_expired(self):
        if self.deadline is not None:
            if timezone.now() > self.deadline:
                return True
            else:
                return False
