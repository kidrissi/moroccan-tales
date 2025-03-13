from rest_framework import serializers
from .models import Story, Like, Comment, Category

class StorySerializer (serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ("id", "title", "content", "author", "image")
        read_only_field = ("id")


class LikeSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Like
        fields = ['id', 'user', 'story', 'created_at'] 
        read_only_fields = ['id', 'user', 'created_at']  
 

class CommentSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source="user.username")
    story = serializers.PrimaryKeyRelatedField(read_only=True)  

    class Meta:
        model = Comment
        fields = ["id", "title", "content", "created_at"]
        read_only_fields = ['id', 'user', 'story', 'created_at']  # Auto-filled fields


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model  = Category
        fields = ["name", "description", "created_at", "updated_at"]




        