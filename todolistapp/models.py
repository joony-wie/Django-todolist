from django.db import models
from django.utils import timezone


class Todo(models.Model):
    # id = models.AutoField(primary_key=True) : Automatic primary key fields in Django
    title = models.CharField(max_length=200)
    text = models.TextField()
    deadline = models.DateTimeField(blank=True, null=True)
    priority = models.PositiveIntegerField(default=1)
    completed = models.BooleanField(default=False)

    #def publish(self):
    #    self.deadline = timezone.now()
    #    self.save()

    def is_completed(self):
        return self.completed
    
    def is_over_deadline(self):
        return timezone.now() < self.deadline

    def __str__(self):
        return self.title
