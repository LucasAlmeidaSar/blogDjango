# Generated by Django 3.2.6 on 2021-08-28 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_post_imagem_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='excerto_post',
            field=models.CharField(max_length=200, verbose_name='Excerto'),
        ),
        migrations.AlterField(
            model_name='post',
            name='titulo_post',
            field=models.CharField(max_length=150, verbose_name='Título post'),
        ),
    ]
