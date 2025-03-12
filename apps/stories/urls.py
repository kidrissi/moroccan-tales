from django.urls import path
from .views import StoryGetView, StoryPostView, StoryUpdateView, StoryDeleteView

urlpatterns = [
    path("list/", StoryGetView.as_view(), name='story-list'),
    path("story/<int:story_id>/", StoryGetView.as_view(), name='story-detail'),
    path("create/", StoryPostView.as_view(), name='story-list'),

    path('story/update/<int:story_id>/', StoryUpdateView.as_view(), name='story-update'),
    path('story/delete/<int:story_id>/', StoryDeleteView.as_view(), name='story-delete'),

]