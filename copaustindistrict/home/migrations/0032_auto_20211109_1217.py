# Generated by Django 3.2.7 on 2021-11-09 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0031_auto_20211109_1207'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='childrenministry',
            options={'verbose_name': 'Children Ministrie'},
        ),
        migrations.AlterModelOptions(
            name='evangelismministry',
            options={'verbose_name': 'Evangelism Ministrie'},
        ),
        migrations.AlterModelOptions(
            name='menministry',
            options={'verbose_name': "Men's Ministrie"},
        ),
        migrations.AlterModelOptions(
            name='womenministry',
            options={'verbose_name': "Women's Ministrie"},
        ),
        migrations.AlterModelOptions(
            name='youthministry',
            options={'verbose_name_plural': 'Youth & Pensa Ministrie'},
        ),
    ]
