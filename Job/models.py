from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class StudentUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=14, null= True)
    resume = models.FileField(null= True)
    gender = models.CharField(max_length=10, null=True)
    type = models.CharField(max_length=18, null=True)
    def _str_(self):
        return self.user.username


class Recruiter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=14, null= True)
    image = models.FileField(null= True)
    gender = models.CharField(max_length=10, null=True)
    company= models.CharField(max_length=10, null=True)
    type = models.CharField(max_length=18, null=True)
    status = models.CharField(max_length=18, null=True)
    def _str_(self):
        return self.user.username

class Jobs(models.Model):
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    title = models.CharField(max_length=10, null=True)
    salary= models.FloatField(max_length=10, null=True)
    image = models.FileField()
    description = models.CharField(max_length=300, null=True)
    experience = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=70, null=True)
    skills = models.CharField(max_length=100, null=True)
    creationdate = models.DateField()
    def _str_(self):
        return self.title


class Apply(models.Model):
    job = models.ForeignKey(Jobs,on_delete=models.CASCADE)
    student =models.ForeignKey(StudentUser,on_delete=models.CASCADE)
    resume = models.FileField(null=True)
    applydate = models.DateField()
    def str(self):
        return self.id

