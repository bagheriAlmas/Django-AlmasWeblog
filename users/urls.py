from django.urls import path
from .views import user_register_view,user_detail_view,user_update_view,reporter_list_view

urlpatterns = [
    path('register/', user_register_view, name='register'),
    path('users/<int:pk>/', user_detail_view, name='user_detail'),
    path('users/<int:pk>/update/', user_update_view, name='user_update'),
    path('users/reporters/', reporter_list_view, name='reporter_list'),
]
