# Generated by Django 3.2.6 on 2021-10-28 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20210827_2222'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=150, null=True, unique=True),
        ),
    ]