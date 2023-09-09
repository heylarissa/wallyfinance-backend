from django.db import models
from user_auth.models import User
from utils.choices import GOAL_TYPE

class GoalsCategory(models.Model):
    category_name = models.CharField(max_length=50)

class Goals(models.Model):
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(User, on_delete=models.RESTRICT)

    name = models.CharField(max_length=50)
    goals_category = models.ForeignKey(GoalsCategory, on_delete=models.SET_NULL, null=True, blank=True)
    goal = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True, default=None)
    periode = models.CharField(max_length=50)
    hit = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)
    goal_type = models.CharField(choices=GOAL_TYPE, max_length=1)