from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from .views import PostViewSet

api_router = DefaultRouter()
api_router.register('posts', PostViewSet)

urlpatterns = [
    path('v1/', include(api_router.urls))
]
