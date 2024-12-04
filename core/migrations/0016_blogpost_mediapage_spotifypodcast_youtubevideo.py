# Generated by Django 5.1.3 on 2024-12-04 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_volunteerapplication_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('featured_image', models.ImageField(upload_to='blog/')),
                ('content', models.TextField()),
                ('excerpt', models.TextField(help_text='Short description for preview', max_length=300)),
                ('author', models.CharField(max_length=100)),
                ('published_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_featured', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-published_date'],
            },
        ),
        migrations.CreateModel(
            name='MediaPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Media Center', max_length=200)),
                ('header_image', models.ImageField(upload_to='media/')),
                ('blog_section_title', models.CharField(default='Latest Blog Posts', max_length=200)),
                ('youtube_section_title', models.CharField(default='Video Messages', max_length=200)),
                ('podcast_section_title', models.CharField(default='Audio Messages', max_length=200)),
            ],
            options={
                'verbose_name': 'Media Page',
                'verbose_name_plural': 'Media Page',
            },
        ),
        migrations.CreateModel(
            name='SpotifyPodcast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('spotify_id', models.CharField(help_text='Spotify episode/track ID', max_length=100)),
                ('published_date', models.DateTimeField()),
                ('duration', models.CharField(help_text='Duration in format MM:SS', max_length=10)),
                ('is_featured', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-published_date'],
            },
        ),
        migrations.CreateModel(
            name='YouTubeVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('video_id', models.CharField(help_text='YouTube video ID from URL', max_length=20)),
                ('published_date', models.DateTimeField()),
                ('is_featured', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-published_date'],
            },
        ),
    ]