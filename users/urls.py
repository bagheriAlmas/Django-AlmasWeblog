from django.urls import path
from .views import user_register_view,user_detail_view

urlpatterns = [
    path('register/', user_register_view, name='register'),
    path('users/<int:pk>/', user_detail_view, name='user_detail'),
]
