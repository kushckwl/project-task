from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    duration = models.DurationField()
    image = models.ImageField(upload_to='img/')

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=50)
    project = models.ForeignKey(Project,default=None, on_delete=CASCADE, related_name='project')
    user = models.ForeignKey(User,default=None, on_delete=CASCADE, related_name='user')
    start_date = models.DateField()
    end_date = models.DateField()

    