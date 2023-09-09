from django.db import models
from user_auth.models import User
from utils.choices import TRANSACTION_TYPES

class Transaction(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    description = models.CharField(max_length=120, blank=False, null=False)
    transaction_owner = models.ForeignKey(User, on_delete=models.RESTRICT)
    transaction_type = models.CharField(max_length=1, choices=TRANSACTION_TYPES, blank=False, null=False)

    class Meta:
        db_table = 'cash_flow'