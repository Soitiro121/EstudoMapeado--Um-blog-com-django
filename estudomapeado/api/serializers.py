from rest_framework import serializers

from telas.models import Texto, Video


class TextoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Texto
        fields = ['title', 'body', 'link', 'created_on', 'last_modified', 'categories']


class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        ['title', 'body', 'link', 'created_on', 'last_modified', 'categories']