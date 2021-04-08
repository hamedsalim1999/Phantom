from django.urls import path,include
from .views import CardInfoListView,CardCommentListCreateAPI
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'', CardInfoListView)
router.register(r'^create$', CardCommentListCreateAPI)
urlpatterns = [
    path('', include(router.urls)),
]


