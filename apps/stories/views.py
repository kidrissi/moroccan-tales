from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.decorators import permission_classes

from rest_framework.response import Response
from .models import Story

from apps.stories.serializerz import StorySerializer


class StoryGetView(APIView):

    permission_classes = [permissions.AllowAny]

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

class StoryPostView(APIView):

    permission_classes=[IsAuthenticated]

    def post(self,request):
        serializer =StorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    



class StoryUpdateView(APIView):

    permission_classes= [IsAuthenticated]

    def put(self, request, pk):
        try:
            story = Story.objects.get(pk=pk, author=request.user)  # Only allow the author to update the story
        except Story.DoesNotExist:
            return Response({"detail": "Story not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StorySerializer(story, data=request.data)
        
        if serializer.is_valid():
            serializer.save()  # Save the updated story
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class StoryDeleteView(APIView):

    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            story = Story.objects.get(pk=pk, author=request.user)
        except Story.DoesNotExist:
            return Response({"detail": "Story not found."}, status=status.HTTP_404_NOT_FOUND)
        return Response({"detail": "Story deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

# Create your views here.


