from django.urls import path
from . import views

app_name = 'post'
urlpatterns = [
    path('', views.post_create, name='create'),
    path('feed/', views.feed, name='feed'),
    path('like/', views.like_post, name='post_like'),
    
]