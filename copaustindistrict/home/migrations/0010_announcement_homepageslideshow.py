# Generated by Django 3.2.7 on 2021-10-26 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_pastormessage_video_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('display', models.BooleanField(default=False)),
                ('level', models.CharField(choices=[('warning', 'Warning'), ('error', 'Error'), ('success', 'Success'), ('info', 'Info')], default='info', max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='HomePageSlideshow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slideshow_image1', models.ImageField(upload_to='')),
                ('slideshow_image2', models.ImageField(upload_to='')),
                ('slideshow_image3', models.ImageField(upload_to='')),
            ],
        ),
    ]
