from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

# app_name = "podapp"
urlpatterns = [
    # e.g. /podapp/
    path('', views.IndexView.as_view(), name="index"),

    # e.g. /podapp/pod/1/
    path('pod/<int:pk>/', views.PodcastView.as_view(), name="podcast"),

    # e.g. /podapp/episodes/1
    path('episodes/<int:pk>', views.EpisodeView.as_view(), name="episode"),

    # e.g. /podapp/add_podcast
    path('add_podcast/', views.add_podcast, name="add_podcast"),

    # class based generic views
    path('pod/add/', views.PodcastCreate.as_view(), name="podcast-add"),
    path('pod/<int:pk>/update/', views.PodcastUpdate.as_view(), name="podcast-update"),
    path('pod/<int:pk>/delete/', views.PodcastDelete.as_view(), name='podcast-delete'),
]
