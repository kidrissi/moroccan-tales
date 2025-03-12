from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.decorators import permission_classes

from rest_framework.response import Response
from .models import Story

from apps.stories.serializerz import StorySerializer


class StoryView(APIView):

    #permission_classes = [permissions.AllowAny]
    @permission_classes(AllowAny)
    def get(self, request, story_id=None):
        """
        Retrieve a list of stories or a single story if story_id is provided.
        """
        if story_id:
            story = get_object_or_404(Story, id=story_id)
            serializer = StorySerializer(story)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            print("test")
            stories = Story.objects.all()
            serializer = StorySerializer(stories, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    @permission_classes(IsAuthenticated)
    def post(self,request):
        serializer =StorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    

# Create your views here.


