import re
from django.db.models import query
from .models import CardComment,CardInfo
from .serializers import CardInfoSerializer,CardCommentSerializer
from rest_framework.generics import ListAPIView,ListCreateAPIView



class CardInfoListView(ListAPIView):
    queryset = CardInfo.objects.all()
    serializer_class = CardInfoSerializer
    

class CardCommentListCreateAPI(ListCreateAPIView):
    queryset = CardComment.objects.all()
    serializer_class = CardCommentSerializer