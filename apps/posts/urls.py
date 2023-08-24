from django.urls import path 

from apps.posts.views import PostAPIView, PostRetrieveAPIView, PostCreateAPIView, PostUpdateAPIView, PostDestroyAPIView


urlpatterns = [
    path('', PostAPIView.as_view(), name='api_posts'),
    path('<int:pk>/', PostRetrieveAPIView.as_view(), name='api_posts_retrieve'),
    path('create/', PostCreateAPIView.as_view(), name='api_posts_create'),
    path('update/<int:pk>/', PostUpdateAPIView.as_view(), name='api_posts_update'),
    path('destroy/<int:pk>/', PostDestroyAPIView.as_view(), name='api_posts_destroy'),
]