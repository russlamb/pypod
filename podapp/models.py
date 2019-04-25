from django.db import models


# Create your models here.


class Podcast(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    link = models.URLField(blank=True)

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
    language = models.CharField(max_length=50, default="en-us")
    copyright = models.CharField(max_length=50, default="All rights reserved")
    email = models.EmailField(blank=True)
    description = models.CharField(max_length=5000, default="Podcast Description")
    image = models.URLField(blank=True)
    author = models.CharField(max_length=200, default="Podcast Author")
    itunes_subtitle = models.CharField(max_length=50, blank=True)
    itunes_type = models.CharField(max_length=50, default="serial")
    itunes_category = models.CharField(max_length=50, choices=ITUNES_CATEGORY, default="Society & Culture")

    # duplicate fields
    # itunes_name: name
    # itunes_email=email

    def __str__(self):
        return self.name


class Episode(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=5000, default="Episode Description")
    file = models.FileField(upload_to='episodes/')
    created_on = models.DateTimeField(auto_now_add=True, blank=True)  #
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE)

    # RSS items below based on iTunes RSS sample
    # https://help.apple.com/itc/podcasts_connect/#/itcbaf351599
    episode_type = models.CharField(max_length=50, default="full")
    episode = models.IntegerField(default=1)  # itunes_episode tag
    season = models.IntegerField(default=1)  # itunes_season tag
    duration_in_seconds = models.IntegerField(default=-1)
    author = models.CharField(max_length=200, default="Episode Author")
    explicit = models.BooleanField(default=False)  # itunes_explicit tag.  should be "yes" or "no"
    enclosure_type = models.CharField(max_length=50, default="audio/mpeg")
    image = models.URLField(blank=True)  # itunes_image tag

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
