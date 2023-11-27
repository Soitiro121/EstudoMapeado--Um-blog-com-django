from django.urls import path
from .views import TextoList, TextoDetail, VideoList, VideoDetail

urlpatterns = [
    path('textos/<int:pk>/', TextoDetail.as_view()),
    path('textos/', TextoList.as_view()),
    path('videos/<int:pk>/', VideoDetail.as_view()),
    path('videos/', VideoList.as_view()),
]