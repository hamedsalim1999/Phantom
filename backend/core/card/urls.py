from django.urls import path
from .views import CardInfoListView,CardCommentListCreateAPI
urlpatterns = [
    path('',CardInfoListView.as_view(),name='main'),
    path('create',CardCommentListCreateAPI.as_view(),name='create'),
]
