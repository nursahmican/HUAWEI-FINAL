# Generated by Django 4.1.4 on 2022-12-28 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('disease', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('normal', models.FloatField(blank=True, null=True)),
                ('other_abnormalities', models.FloatField(blank=True, null=True)),
                ('pathological_myopia', models.FloatField(blank=True, null=True)),
                ('hypertension', models.FloatField(blank=True)),
                ('glaucoma', models.FloatField(blank=True, null=True)),
                ('diabetes', models.FloatField(blank=True, null=True)),
                ('cataract', models.FloatField(blank=True, null=True)),
                ('age_related_macular_degeneration', models.FloatField(blank=True, null=True)),
                ('image', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='disease.image')),
            ],
        ),
    ]
