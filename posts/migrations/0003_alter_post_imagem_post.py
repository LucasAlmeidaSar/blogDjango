# Generated by Django 3.2.6 on 2021-08-28 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_data_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagem_post',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Imagem do post'),
        ),
    ]
