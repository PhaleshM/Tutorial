from django.shortcuts import render
from .models import Video
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
class VideoListView(ListView):
    model = Video    
    # Default assume videos/template/videos/video_list.html exists.
    queryset = Video.objects.order_by('title')


class VideoThumbsView(ListView):
    model = Video 
    # we specify a different template for the ListView
    template_name="videos/video_thumbs.html"
    # alternative to video_thumbs in place of object_list
    context_object_name='video_thumbs'
    # function to sort the videos 
    def get_queryset(self):
    
        return Video.objects.filter(category_id = self.kwargs['category_id']).filter(is_active=True)

class VideoDetailView(DetailView):
    model = Video
    # Default assume videos/template/videos/video_detail.html exists.

class VideoCreateView(SuccessMessageMixin,CreateView):
    model = Video
    fields=['title','author', 'discription','youtube_vid', 'star_count','category_id', 'skill_level','is_active']
    # template_name = ".html"
    # Default assume videos/template/videos/video_form.html exists.
    # Send back to video list on succesful save
    success_url=reverse_lazy("video-list")
    success_message="VIDEO ADDED!"


class VideoUpdateView(SuccessMessageMixin,UpdateView):
    model = Video
    fields=['title','author', 'discription','youtube_vid', 'star_count','category_id', 'skill_level','is_active']
    # template_name = ".html"
    # Default assume videos/template/videos/video_form.html exists.
    # Send back to video list on succesful save
    success_url=reverse_lazy("video-list")
    success_message="VIDEO UPDATED!"

class VideoDeleteView(SuccessMessageMixin,DeleteView):
    model = Video
    # Default assume videos/template/videos/video_confirm_delete.html exists.
    # Send back to video list on succesful save
    success_url=reverse_lazy("video-list")
    success_message="VIDEO DELETED!"

    
