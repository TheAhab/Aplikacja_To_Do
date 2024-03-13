from django.db import models

class Tag(models.Model):
    Name = models.CharField(max_length=20)
    
    # def __str__(self):
    #     return self.Name

class Task(models.Model):
    Name = models.CharField(max_length=50)
    Tags = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.Name

class Date(models.Model):
    Day = models.IntegerField()
    Tasks = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True)