from django.urls import path,include
from .views import home
from .api.api_views import UserAccountViewSet, PostViewSet, UserPostsViewSet, CreateUserViewSet
from rest_framework import routers, serializers, viewsets

router = routers.DefaultRouter()
router.register(r'users', UserAccountViewSet)
router.register(r'posts', PostViewSet)

urlpatterns = [
    path("",home),
    path('api/', include(router.urls)),
    path('api/userposts/<int:user_id>/', UserPostsViewSet.as_view()),
    path('api/create_user/', CreateUserViewSet.as_view()),
]