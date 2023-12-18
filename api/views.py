from rest_framework import generics

from telas.models import Texto, Video, ForumMessage
from .serializers import TextoSerializer, VideoSerializer, ForumMessageSerializer


class TextoList(generics.ListCreateAPIView):
    queryset = Texto.objects.all()
    serializer_class = TextoSerializer


class TextoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Texto.objects.all()
    serializer_class = TextoSerializer

class VideoList(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    
class VideoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class ForumMessageList(generics.ListCreateAPIView):
    queryset = ForumMessage.objects.all()
    serializer_class = ForumMessageSerializer
    
class ForumMessageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ForumMessage.objects.all()
    serializer_class = ForumMessageSerializer