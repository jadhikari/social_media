from django.urls import path
from . import views

app_name = 'post'
urlpatterns = [
    path('', views.post_create, name='create'),
    
]