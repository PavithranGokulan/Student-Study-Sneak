from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Notes(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title= models.CharField(max_length=200)
    description=models.TextField(null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True)

class NoteApp(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title= models.CharField(max_length=200)
    content=models.TextField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title',)

class Task(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title= models.CharField(max_length=200)
    description=models.TextField(null=True,blank=True)
    complete=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



    class Meta:
        ordering = ['complete']


class Remainder(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField(default=datetime.date.today())
    time = models.TimeField(default=datetime.time())