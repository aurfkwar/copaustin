# Generated by Django 3.2.7 on 2021-10-28 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_auto_20211028_0339'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcementpage',
            name='announcement_title',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
