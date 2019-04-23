from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import  views

urlpatterns = [
    # e.g. /podapp/
    path('', views.index, name="index"),
    # e.g. /podapp/podcast/1/
    path('podcast/<int:podcast_id>/',views.episodes, name="episodes"),
    # e.g. /podapp/episodes/1
    path('episodes/<int:episode_id>',views.episode, name="episode"),
]

