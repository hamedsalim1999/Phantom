from django.db import models
from django.utils import timezone
# base models for all models need crate and updated date
class Timestamp(models.Model):
    create = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True) 
    class Meta:
        abstract = True



