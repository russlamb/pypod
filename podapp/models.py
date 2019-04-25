from django.db import models
from django.urls import reverse

# Create your models here.


class Podcast(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    name = models.CharField(max_length=100, unique=True, verbose_name="Name")
    link = models.URLField(blank=True, verbose_name="Podcast URL")

    # Choices
    ITUNES_CATEGORY = (
        ("Arts", "Arts"),
        ("Business", "Business"),
        ("Comedy", "Comedy"),
        ("Education", "Education"),
        ("Games & Hobbies", "Games & Hobbies"),
        ("Government & Organizations", "Government & Organizations"),
        ("Health", "Health"),
        ("Music", "Music"),
        ("News & Politics", "News & Politics"),
        ("Religion & Spirituality", "Religion & Spirituality"),
        ("Science & Medicine", "Science & Medicine"),
        ("Society & Culture", "Society & Culture"),
        ("Sports & Recreation", "Sports & Recreation"),
        ("Technology", "Technology"),
    )

    # RSS items below based on iTunes RSS sample
    # https://help.apple.com/itc/podcasts_connect/#/itcbaf351599
    language = models.CharField(max_length=50, default="en-us", verbose_name="Podcast Language")
    copyright = models.CharField(max_length=50, default="All rights reserved", verbose_name="Copyright")
    email = models.EmailField(blank=True, verbose_name="Contact Email")
    description = models.CharField(max_length=5000, default="Podcast Description", verbose_name="Description")
    image = models.URLField(blank=True, verbose_name="Podcast Cover Image")
    author = models.CharField(max_length=200, default="Podcast Author", verbose_name="Podcast Author")
    itunes_subtitle = models.CharField(max_length=50, blank=True, verbose_name="Subtitle")
    itunes_type = models.CharField(max_length=50, default="serial", verbose_name="iTunes Type")
    itunes_category = models.CharField(max_length=50, choices=ITUNES_CATEGORY, default="Society & Culture",
                                       verbose_name="iTunes Category")

    # duplicate fields
    # itunes_name: name
    # itunes_email=email

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('podcast', kwargs={'pk': self.pk})

class Episode(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    title = models.CharField(max_length=100, unique=True, verbose_name="Episode Title")
    description = models.CharField(max_length=5000, default="Episode Description", verbose_name="Description")
    file = models.FileField(upload_to='episodes/', verbose_name="Episode File")
    created_on = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Created On")  #
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE, verbose_name="Podcast")

    # RSS items below based on iTunes RSS sample
    # https://help.apple.com/itc/podcasts_connect/#/itcbaf351599
    episode_type = models.CharField(max_length=50, default="full", verbose_name="Episode Type")
    episode = models.IntegerField(default=1, verbose_name="Episode Number")  # itunes_episode tag
    season = models.IntegerField(default=1, verbose_name="Season Number")  # itunes_season tag
    duration_in_seconds = models.IntegerField(default=-1, verbose_name="Duration of Episode")
    author = models.CharField(max_length=200, default="Episode Author", verbose_name="Episode Author")
    explicit = models.BooleanField(default=False, verbose_name="Explicit Content")  # itunes_explicit tag.  should be "yes" or "no"
    enclosure_type = models.CharField(max_length=50, default="audio/mpeg", verbose_name="Enclosure Type")
    image = models.URLField(blank=True, verbose_name="Episode Cover Image")  # itunes_image tag

    # duplicate tags not implemented and their equivalents
    # enclosure_url: file.url
    # guid: file.url
    # itunes_summary: description
    # itunes_title: title
    # enclosure_length: duration_in_seconds
    # itunes_duration: duration_in_seconds
    # pubDate: created_on

    def __str__(self):
        return "{}-{}".format(self.podcast, self.title)
