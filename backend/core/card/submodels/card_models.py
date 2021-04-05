from django.db import models
from django.db.models.fields import TextField
from .base_modles import Timestamp

class CardInfo(Timestamp):
    name = models.CharField(max_length=256)
    description = models.TextField()
    image = models.ImageField(max_length=128,upload_to='card/image', height_field='height_field', width_field='width_field',blank=True, null=True)
    height_field = models.PositiveIntegerField(default='480',blank=True, null=True)
    width_field  = models.PositiveIntegerField(default='720',blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:

        verbose_name = 'CardInfo'
        verbose_name_plural = 'CardInfoes'