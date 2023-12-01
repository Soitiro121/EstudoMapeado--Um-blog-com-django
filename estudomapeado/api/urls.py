from django.urls import path
from .views import TextoList, TextoDetail, VideoList, VideoDetail, ForumMessageList, ForumMessageDetail

urlpatterns = [
    path('textos/<int:pk>/', TextoDetail.as_view()),
    path('textos/', TextoList.as_view()),
    path('videos/<int:pk>/', VideoDetail.as_view()),
    path('videos/', VideoList.as_view()),
    path('videos/<int:pk>/', VideoDetail.as_view()),
    path('videos/', VideoList.as_view()),
    path('forummessages/', ForumMessageList.as_view()),
    path('forummessages/<int:pk>/', ForumMessageDetail.as_view()),
]