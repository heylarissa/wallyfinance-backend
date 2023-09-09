from django.db import models
from user_auth.models import User
from django.contrib.auth.models import Group

# Create your models here.
class BankAccount (models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    account_balance = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True, default=None)
    holder = models.ForeignKey(User,on_delete=models.RESTRICT)