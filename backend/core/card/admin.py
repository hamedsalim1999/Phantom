from django.contrib import admin
from .models import CardInfo,CardComment
# Register your models here.

@admin.register(CardInfo)
class CardInfoAdmin(admin.ModelAdmin):
    '''Admin View for CardInfo'''
    pass

@admin.register(CardComment)
class CardCommentAdmin(admin.ModelAdmin):
    '''Admin View for CardComment'''

    pass