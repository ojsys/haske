# Generated by Django 5.1.3 on 2024-12-03 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_aboutministry_options_aboutministry_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutpage',
            name='ministry_goal',
            field=models.TextField(default='Our Goal', help_text='Main Goal'),
        ),
    ]
