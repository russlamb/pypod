# Generated by Django 2.2 on 2019-04-16 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='file',
            field=models.FileField(upload_to='episodes/'),
        ),
    ]
