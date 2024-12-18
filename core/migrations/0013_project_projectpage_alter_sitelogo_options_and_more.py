# Generated by Django 5.1.3 on 2024-12-03 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_aboutpage_ministry_goal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='projects/')),
                ('order', models.IntegerField(default=0)),
                ('beneficiaries', models.IntegerField(default=0)),
                ('location', models.CharField(blank=True, max_length=200)),
                ('date', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Projects',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='ProjectPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='HASKE PROJECTS', max_length=200)),
                ('header_image', models.ImageField(help_text='Header image for projects page', upload_to='projects/')),
                ('introduction', models.TextField(help_text='Introduction text below header')),
            ],
            options={
                'verbose_name': 'Project Page',
                'verbose_name_plural': 'Project Page',
            },
        ),
        migrations.AlterModelOptions(
            name='sitelogo',
            options={'verbose_name_plural': 'Site Logo'},
        ),
        migrations.AlterField(
            model_name='missionvision',
            name='mission_image',
            field=models.ImageField(help_text='Image for Mission', upload_to='about/'),
        ),
        migrations.AlterField(
            model_name='missionvision',
            name='vision_image',
            field=models.ImageField(help_text='Image for Vision', upload_to='about/'),
        ),
    ]
