from django.db import models
from django.contrib.auth.models import User
from contest.models import Contest
# Create your models here.
# problem model

class Problem(models.Model):
    name = models.CharField(max_length=125,null=True)
    tag = models.CharField(max_length=50,null=True)
    contest=models.ForeignKey(Contest,on_delete=models.CASCADE,null=True)
    discription = models.TextField(null=True)
    time_complexity = models.CharField(max_length=50,null=True)
    space_complexity = models.CharField(max_length=50,null=True)
    example = models.TextField(null=True)
    total_submission=models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.name

# testcase model
class TestCase(models.Model):
    input = models.TextField(null=True)
    output = models.TextField(null=True)
    problem = models.ForeignKey(Problem,on_delete=models.CASCADE,null=True)

# submission model
class Submission(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    contest=models.ForeignKey(Contest,on_delete=models.CASCADE)
    problem=models.ForeignKey(Problem,on_delete=models.CASCADE,null=True)
    submitted_time=models.TimeField()
    verdict=models.CharField(max_length=50)
    lang=models.CharField(max_length=50,null=True)
    code = models.TextField(null=True)
    def __str__(self) -> str:
        return self.user.username
