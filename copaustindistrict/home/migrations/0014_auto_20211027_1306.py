# Generated by Django 3.2.7 on 2021-10-27 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20211027_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcementpage',
            name='body',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='homepageslideshow',
            name='slideshow_image1',
            field=models.ImageField(blank='True', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='homepageslideshow',
            name='slideshow_image2',
            field=models.ImageField(blank='True', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='homepageslideshow',
            name='slideshow_image3',
            field=models.ImageField(blank='True', upload_to='images/'),
        ),
    ]
