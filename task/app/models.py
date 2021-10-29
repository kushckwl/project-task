from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    duration = models.DurationField()
    image = models.ImageField()

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()

    