# Generated by Django 2.2 on 2019-04-24 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podapp', '0002_auto_20190416_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='author',
            field=models.CharField(default='Episode Author', max_length=200),
        ),
        migrations.AddField(
            model_name='episode',
            name='duration_in_seconds',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='episode',
            name='enclosure_type',
            field=models.CharField(default='audio/mpeg', max_length=50),
        ),
        migrations.AddField(
            model_name='episode',
            name='episode',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='episode',
            name='episode_type',
            field=models.CharField(default='full', max_length=50),
        ),
        migrations.AddField(
            model_name='episode',
            name='explicit',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='episode',
            name='image',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='episode',
            name='season',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='podcast',
            name='author',
            field=models.CharField(default='Podcast Author', max_length=200),
        ),
        migrations.AddField(
            model_name='podcast',
            name='copyright',
            field=models.CharField(default='All rights reserved', max_length=50),
        ),
        migrations.AddField(
            model_name='podcast',
            name='description',
            field=models.CharField(default='Podcast Description', max_length=5000),
        ),
        migrations.AddField(
            model_name='podcast',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='podcast',
            name='image',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='podcast',
            name='itunes_category',
            field=models.CharField(choices=[('Arts', 'Arts'), ('Business', 'Business'), ('Comedy', 'Comedy'), ('Education', 'Education'), ('Games & Hobbies', 'Games & Hobbies'), ('Government & Organizations', 'Government & Organizations'), ('Health', 'Health'), ('Music', 'Music'), ('News & Politics', 'News & Politics'), ('Religion & Spirituality', 'Religion & Spirituality'), ('Science & Medicine', 'Science & Medicine'), ('Society & Culture', 'Society & Culture'), ('Sports & Recreation', 'Sports & Recreation'), ('Technology', 'Technology')], default='Society & Culture', max_length=50),
        ),
        migrations.AddField(
            model_name='podcast',
            name='itunes_subtitle',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='podcast',
            name='itunes_type',
            field=models.CharField(default='serial', max_length=50),
        ),
        migrations.AddField(
            model_name='podcast',
            name='language',
            field=models.CharField(default='en-us', max_length=50),
        ),
        migrations.AddField(
            model_name='podcast',
            name='link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='episode',
            name='description',
            field=models.CharField(default='Episode Description', max_length=5000),
        ),
    ]
