from django.db import models

# Create your models here.
class Task(models.Model):
    task_name = models.CharField(max_length=100)

    def __str__(self):
        return self.task_name
    
class Assigned_person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=254)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    def __str__(self):
        return self.first_name