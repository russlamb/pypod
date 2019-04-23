from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
# Create your views here.
from .models import Podcast, Episode

def index(request):
    podcast_list = Podcast.objects.all()
    context = {'podcast_list':podcast_list}
    return render(request, 'podapp/index.html', context)

def episodes(request, podcast_id):
    podcast = get_object_or_404(Podcast, pk=podcast_id)

    episode_list = podcast.episode_set.all()
    context = {'episode_list':episode_list, "podcast_name":podcast.name, "podcast_id":podcast.id}
    return render(request, 'podapp/episodes.html', context)


def episode(request,  episode_id):
    episode = get_object_or_404(Episode,pk=episode_id)
    context = {"episode":episode}
    return render(request, "podapp/episode_detail.html", context)
