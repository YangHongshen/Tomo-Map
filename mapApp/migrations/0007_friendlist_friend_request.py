# Generated by Django 3.0.3 on 2020-06-07 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapApp', '0006_friendlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='friendlist',
            name='friend_request',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
