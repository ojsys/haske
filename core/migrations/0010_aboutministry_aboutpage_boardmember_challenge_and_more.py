# Generated by Django 5.1.3 on 2024-12-03 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_subscriber'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMinistry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Ministries',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='ABOUT US', max_length=200)),
                ('header_image', models.ImageField(help_text='Header image for about page', upload_to='about/')),
                ('introduction', models.TextField(help_text='Main introduction text')),
            ],
            options={
                'verbose_name': 'About Page',
                'verbose_name_plural': 'About Page',
            },
        ),
        migrations.CreateModel(
            name='BoardMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
                ('bio', models.TextField()),
                ('image', models.ImageField(upload_to='board/')),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('order', models.IntegerField(default=0)),
                ('challenge1_title', models.CharField(default='Reaching the Unreached in 10/40 Window', max_length=200)),
                ('challenge1_desc', models.TextField()),
                ('challenge1_image', models.ImageField(help_text='Challenge Image', upload_to='about/challenge/')),
                ('challenge2_title', models.CharField(default='Praying for the Unreached', max_length=200)),
                ('challenge2_desc', models.TextField()),
                ('challenge2_image', models.ImageField(help_text='Challenge Image', upload_to='about/challenge/')),
                ('challenge3_title', models.CharField(default='Supporting Education in Nigeria', max_length=200)),
                ('challenge3_desc', models.TextField()),
                ('challenge3_image', models.ImageField(help_text='Challenge Image', upload_to='about/challenge/')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='MissionVision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mission_title', models.CharField(default='Our Mission', max_length=200)),
                ('mission_text', models.TextField()),
                ('vision_title', models.CharField(default='Our Vision', max_length=200)),
                ('vision_text', models.TextField()),
                ('mission_image', models.ImageField(height_field='Image for Mission', upload_to='about/')),
                ('vision_image', models.ImageField(height_field='Image for Vision', upload_to='about/')),
            ],
            options={
                'verbose_name': 'Mission and Vision',
                'verbose_name_plural': 'Mission and Vision',
            },
        ),
    ]
