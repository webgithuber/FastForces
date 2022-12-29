from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#contest model

class Contest(models.Model):
   name=models.CharField(max_length=50,null=True)
   start_time=models.DateTimeField(null=True, blank=True)
   end_time=models.DateTimeField(null=True, blank=True)
   duration=models.DurationField(null=True, blank=True)
   registered_user=models.IntegerField(default=0)
   a_score=models.IntegerField(default=10)
   b_score=models.IntegerField(default=20)
   c_score=models.IntegerField(default=30)
   d_score=models.IntegerField(default=50)

   def __str__(self) -> str:
      return self.name


# registered_contestant model
class RegisteredContestant(models.Model):
    contest=models.ForeignKey(Contest,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    a_score=models.IntegerField(default=0)
    b_score=models.IntegerField(default=0)
    c_score=models.IntegerField(default=0)
    d_score=models.IntegerField(default=0)
    total_score=models.IntegerField(default=0)
