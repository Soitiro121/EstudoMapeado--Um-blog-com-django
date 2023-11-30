from rest_framework import serializers
from django.contrib.auth.models import User
from telas.models import Texto, Video, ForumMessage


class TextoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Texto
        fields = ['title', 'body', 'link', 'created_on', 'categories']


class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        ['title', 'body', 'link', 'created_on', 'last_modified', 'categories']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class ForumMessageSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # Serialize the user field using the UserSerializer

    class Meta:
        model = ForumMessage
        fields = ['id', 'user', 'message', 'timestamp']