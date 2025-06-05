from rest_framework import routers
from django.urls import path, include
from author.views import AuthorViewSet

router = routers.SimpleRouter()
router.register("author", AuthorViewSet)

urlpatterns = [
    path("", include(router.urls))
]

app_name = "author_service"
