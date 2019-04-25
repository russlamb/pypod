from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
# Create your views here.
from .models import Podcast, Episode
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView


class IndexView(generic.ListView):
    template_name = 'podapp/index.html'
    context_object_name = 'podcast_list'

    def get_queryset(self):
        return Podcast.objects.all()


class PodcastView(generic.DetailView):
    model = Podcast
    template_name = 'podapp/podcast_detail.html'


class PodcastCreate(CreateView):
    model = Podcast
    fields = ['name', 'link', 'language', 'copyright', 'email', 'description', 'image', 'author', 'itunes_subtitle',
              'itunes_type', 'itunes_category']


class PodcastUpdate(UpdateView):
    model = Podcast
    fields = ['name', 'link', 'language', 'copyright', 'email', 'description', 'image', 'author', 'itunes_subtitle',
              'itunes_type', 'itunes_category']


class PodcastDelete(DeleteView):
    model = Podcast
    success_url = reverse_lazy('index')


def episode(request, episode_id):
    episode = get_object_or_404(Episode, pk=episode_id)
    context = {"episode": episode}
    return render(request, "podapp/episode_detail.html", context)


class EpisodeView(generic.DetailView):
    model = Episode
    template_name = 'podapp/episode_detail.html'


def add_podcast(request):
    try:
        if request.method == "POST":  # if we have a podcast to add, process it
            p = Podcast(name=request.POST['name'])
            p.save()
        else:  # if we don't have POST data, just render the form
            return render(request, 'podapp/add_podcast.html', {})
    except Exception as ex:  # Redisplay the form
        context = {"error_message": "There was a problem adding that podcast. {}".format(ex)}
        return render(request, 'podapp/add_podcast.html', context)
    else:
        return HttpResponseRedirect(reverse('index'))
