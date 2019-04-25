from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from .models import Podcast, Episode
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'podapp/index.html'
    context_object_name = 'podcast_list'
    def get_queryset(self):
        return Podcast.objects.all()


class PodcastView(generic.DetailView):
    model = Podcast
    template_name = 'podapp/podcast_detail.html'


def episodes(request, podcast_id):
    podcast = get_object_or_404(Podcast, pk=podcast_id)

    episode_list = podcast.episode_set.all()
    context = {'episode_list': episode_list, "podcast_name": podcast.name, "podcast_id": podcast.id}
    return render(request, 'podapp/episodes.html', context)

def episode(request, episode_id):
    episode = get_object_or_404(Episode, pk=episode_id)
    context = {"episode": episode}
    return render(request, "podapp/episode_detail.html", context)

class EpisodeView(generic.DetailView):
    model = Episode
    template_name = 'podapp/episode_detail.html'

def add_podcast(request):
    try:
        if request.method=="POST": # if we have a podcast to add, process it
            p = Podcast(name=request.POST['name'])
            p.save()
        else:   # if we don't have POST data, just render the form
            return render(request, 'podapp/add_podcast.html', {})
    except Exception as ex:  # Redisplay the form
        context = {"error_message": "There was a problem adding that podcast. {}".format(ex)}
        return render(request, 'podapp/add_podcast.html', context)
    else:
        return HttpResponseRedirect(reverse('index'))

