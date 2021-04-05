from django.db import models
from django.db.models.fields import TextField
from .base_modles import Timestamp
from .card_models import CardInfo

class CardComment(Timestamp):
    for_card = models.ForeignKey(CardInfo)
    name = models.CharField(max_length=515,null=True,blank=True)
    body = models,TextField()

    def __str__(self):
        return self.for_card
