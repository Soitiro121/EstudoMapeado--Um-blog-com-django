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


from rest_framework import serializers
from django.contrib.auth.models import User
from telas.models import ForumMessage

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class ForumMessageSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Set read_only=True for the nested user field

    class Meta:
        model = ForumMessage
        fields = ['id', 'user', 'message', 'timestamp']

    def create(self, validated_data):
        # Explicitly create the ForumMessage instance, setting the user from the request
        user = self.context['request'].user
        forum_message = ForumMessage.objects.create(user=user, **validated_data)
        return forum_message
