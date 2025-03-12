from django.urls import path
from .views import StoryView

urlpatterns = [
    path("list/", StoryView.as_view(), name='story-list-create'),
    path("story/<int:story_id>/", StoryView.as_view(), name='story-detail')

]