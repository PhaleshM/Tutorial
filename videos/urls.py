from django.urls import path
from .views import VideoListView, VideoThumbsView, VideoDetailView,VideoCreateView,VideoUpdateView,VideoDeleteView

urlpatterns = [
    path('list/', VideoListView.as_view(), name='video-list'),
    path('thumbs/<int:category_id>', VideoThumbsView.as_view(), name='video-thumbs'),
    path('detail/<int:pk>', VideoDetailView.as_view(), name='video-detail'),
    path('create/', VideoCreateView.as_view(), name='video-create'),
    path('update/<int:pk>', VideoUpdateView.as_view(), name='video-update'),
    path('delete/<int:pk>', VideoDeleteView.as_view(), name='video-delete'),
]