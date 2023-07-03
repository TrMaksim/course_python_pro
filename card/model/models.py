import uuid
from django.db import models


class Cards(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pan = models.CharField(max_length=20)
    expiry_date = models.CharField(max_length=20)
    cvv = models.CharField(max_length=4)
    issue_date = models.DateTimeField(auto_now_add=True)
    owner_id = models.UUIDField(default=uuid.uuid4)
    status = models.CharField(max_length=20)
