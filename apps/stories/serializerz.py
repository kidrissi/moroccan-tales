from rest_framework import serializers
from .models import Story

class StorySerializer (serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ("id", "title", "content", "author", "image")
        read_only_field = ("id")
