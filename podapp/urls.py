from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

#app_name = "podapp"
urlpatterns = [
    # e.g. /podapp/
    # path('', views.index, name="index"),
    path('', views.IndexView.as_view(), name="index"),

    # e.g. /podapp/podcast/1/
    #path('podcast/<int:podcast_id>/', views.episodes, name="episodes"),
    path('pod/<int:pk>/',views.PodcastView.as_view(), name="podcast"),

    # e.g. /podapp/episodes/1
    # path('episodes/<int:episode_id>',views.episode, name="episode"),
    path('episodes/<int:pk>', views.EpisodeView.as_view(), name="episode"),

    # e.g. /podapp/add_podcast
    path('add_podcast/', views.add_podcast, name="add_podcast"),
    # path('add_podcast/',views.AddPodcastView, name="add_podcast"),
]
