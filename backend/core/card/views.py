from django.shortcuts import render

from .models import CardComment,CardInfo
from .serializers import CardCommentSerializer,CardInfoSerializer

from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class CardInfoListView(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = CardInfo.objects.all()
    serializer_class = CardInfoSerializer
class CardCommentListCreateAPI(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = CardComment.objects.all()
    serializer_class = CardCommentSerializer
    

