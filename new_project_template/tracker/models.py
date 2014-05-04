from django.db import models
from datetime import datetime    
###SHould be attached to google users
from django.contrib.auth.models import User
###SHould be attached to google users


class Entry(models.Model):
    task_description = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=datetime.now())
    hours = models.DecimalField(max_digits=4,decimal_places=2)
    #project
    #task 
    #Event

class Project(models.Model):
    project_name= models.CharField(max_length=200)
    project_description = models.CharField(max_length=200)
    project_code = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=datetime.now())
    #user = models.ForeignKey(User)

class Task(models.Model):
    task_name = models.CharField(max_length=200)
    task_description = models.CharField(max_length=200)
    task_code = models.CharField(max_length=200)
    estimated_time = models.DecimalField(max_digits=4,decimal_places=2) # recommend 16
    parent = models.ForeignKey('self',blank=True, null=True)
    user = models.ForeignKey(User,null=True, blank=True, default = None)
    #percentage
    #status choices
    def __unicode__(self):
	#you should add parent Task Name
	return self.task_name #+ " - " + parent_name

class Event(models.Model):
    pub_date = models.DateTimeField(default=datetime.now())
    event_description = models.CharField(max_length=200)
    #document


# Create your models here.
