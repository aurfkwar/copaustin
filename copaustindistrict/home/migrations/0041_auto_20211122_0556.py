# Generated by Django 3.2.7 on 2021-11-22 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0040_alter_announcementpage_announcementimg4'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcementpage',
            name='announcementImg2',
        ),
        migrations.RemoveField(
            model_name='announcementpage',
            name='announcementImg3',
        ),
        migrations.RemoveField(
            model_name='announcementpage',
            name='announcementImg4',
        ),
    ]
