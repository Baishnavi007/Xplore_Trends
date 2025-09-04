from django.db import models
import uuid

class TrendRun(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    trend1 = models.CharField(max_length=255)
    trend2 = models.CharField(max_length=255)
    trend3 = models.CharField(max_length=255)
    trend4 = models.CharField(max_length=255)
    trend5 = models.CharField(max_length=255)
    ip_address = models.GenericIPAddressField()
    scraped_at = models.DateTimeField(auto_now_add=True)
# Create your models here.
