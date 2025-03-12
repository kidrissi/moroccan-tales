from rest_framework.test import APIClient
import pytest
from apps.accounts.models import User
from apps.stories.models import Story

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_user():
    return User.objects.create(username="brave",email="brave@email.com")

@pytest.fixture
def create_stories(create_user):
    user = User.objects.get()
    Story.objects.create(title="what is brave",
                                content="brave can be a man quality or a browser",
                                author=user)
    Story.objects.create(title="what is coward",
                                content="coward can be only you",
                                author=user)

@pytest.mark.django_db
def test_list_stories(create_stories):
    stories = Story.objects.all()

    assert stories.count()==2