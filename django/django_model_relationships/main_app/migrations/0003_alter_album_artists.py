# Generated by Django 4.2.7 on 2023-11-16 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_artist_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='artists',
            field=models.ManyToManyField(related_name='album', to='main_app.artist'),
        ),
    ]