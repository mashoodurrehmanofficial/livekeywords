from django.urls import path
from .views import keyword_fetcher,youtube_video_tags

urlpatterns = [
    path('',keyword_fetcher, name='keyword_fetcher'), 
    path('youtube_video_tags/',youtube_video_tags, name='youtube_video_tags'), 
]
