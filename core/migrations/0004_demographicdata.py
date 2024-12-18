# Generated by Django 5.1.3 on 2024-11-23 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_achievement_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DemographicData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('AB', 'Abia'), ('AD', 'Adamawa'), ('AI', 'Akwa Ibom'), ('AR', 'Anambra'), ('BH', 'Bauchi'), ('BL', 'Bayelsa'), ('BE', 'Benue'), ('BN', 'Borno'), ('CR', 'Cross River'), ('DT', 'Delta'), ('EY', 'Ebonyi'), ('ED', 'Edo'), ('EI', 'Ekiti'), ('EU', 'Enugu'), ('AU', 'FCT - Abuja'), ('GB', 'Gombe'), ('IO', 'Imo'), ('JW', 'Jigawa'), ('KD', 'Kaduna'), ('KO', 'Kano'), ('KA', 'Katsina'), ('KB', 'Kebbi'), ('KG', 'Kogi'), ('KW', 'Kwara'), ('LA', 'Lagos'), ('NW', 'Nasarawa'), ('NG', 'Niger'), ('OG', 'Ogun'), ('OD', 'Ondo'), ('ON', 'Osun'), ('OY', 'Oyo'), ('PU', 'Plateau'), ('RI', 'Rivers'), ('ST', 'Sokoto'), ('TA', 'Taraba'), ('YE', 'Yobe'), ('ZA', 'Zamfara')], max_length=50)),
                ('lga', models.CharField(max_length=100, verbose_name='L.G.A')),
                ('ward', models.CharField(max_length=100)),
                ('village', models.CharField(max_length=100)),
                ('christian_population', models.IntegerField(verbose_name='Christian Population')),
                ('muslim_population', models.IntegerField(verbose_name='Muslim Population')),
                ('traditional_population', models.IntegerField(verbose_name='Traditional People Population')),
                ('converts', models.IntegerField()),
                ('total_village_population', models.IntegerField(verbose_name='Total Village Population')),
                ('film_attendance', models.IntegerField()),
                ('people_group', models.CharField(max_length=100)),
                ('practiced_religion', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Demographic Data',
                'indexes': [models.Index(fields=['state'], name='core_demogr_state_4d6a10_idx'), models.Index(fields=['lga'], name='core_demogr_lga_0d180d_idx')],
                'unique_together': {('state', 'lga', 'ward', 'village')},
            },
        ),
    ]
