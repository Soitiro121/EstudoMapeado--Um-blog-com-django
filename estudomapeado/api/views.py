from rest_framework import generics

from telas.models import Texto, Video
from .serializers import TextoSerializer, VideoSerializer


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