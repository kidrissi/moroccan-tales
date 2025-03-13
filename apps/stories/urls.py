from django.urls import path, include
from .views import StoryGetView, StoryPostView, StoryUpdateView, StoryDeleteView, CategoryViewSet,LikeView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", CategoryViewSet)
urlpatterns = [
    path("list/", StoryGetView.as_view(), name='story-list'),
    path("story/<int:story_id>/", StoryGetView.as_view(), name='story-detail'),
    path("create/", StoryPostView.as_view(), name='story-list'),

    path('story/update/<int:story_id>/', StoryUpdateView.as_view(), name='story-update'),
    path('story/delete/<int:story_id>/', StoryDeleteView.as_view(), name='story-delete'),
    path("categories/",include(router.urls)),
    path('story/<int:story_id>/like',LikeView.as_view(), name="like-story"),
    path('story/<int:story_id>/comment',commentView.as_view(), name="comment-story")




]