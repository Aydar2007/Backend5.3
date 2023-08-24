from django.urls import path 

from apps.users.views import UserAPIView, UserRetrieveAPIView, UserCreateAPIView, UserUpdateAPIView, UserDestroyAPIView


urlpatterns = [
    path('', UserAPIView.as_view(), name="api_users"),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name="api_users_retrieve"),
    path('register/', UserCreateAPIView.as_view(), name="api_users_create"),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name="api_users_update"),
    path('destroy/<int:pk>/', UserDestroyAPIView.as_view(), name="api_users_destroy"),
]