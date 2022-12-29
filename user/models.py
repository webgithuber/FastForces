from django.db import models
from django.contrib.auth.models import User



# user_detail model
class UserDetail(models.Model):

    problems_solved = models.IntegerField(default=0)
    score=models.IntegerField(default=0)
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username