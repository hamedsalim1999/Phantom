from rest_framework import serializers
from .models import CardInfo,CardComment

class CardInfoSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = CardInfo
       exclude = ['updated','create']

class CardCommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
       model = CardComment
       exclude = ['updated','create']