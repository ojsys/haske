# Generated by Django 5.1.3 on 2024-12-04 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_blogpost_mediapage_spotifypodcast_youtubevideo'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(max_length=100)),
                ('account_number', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ContactSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='DonationPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='GIVE', max_length=200)),
                ('header_image', models.ImageField(upload_to='donations/')),
                ('description', models.TextField()),
                ('bank_name', models.CharField(default='Zenith Bank Plc.', max_length=100)),
            ],
            options={
                'verbose_name': 'Donation Page',
                'verbose_name_plural': 'Donation Page',
            },
        ),
    ]
