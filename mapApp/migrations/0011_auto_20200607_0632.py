# Generated by Django 3.0.3 on 2020-06-07 06:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mapApp', '0010_auto_20200607_0214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendlist',
            name='friend',
            field=models.ForeignKey(blank=True, max_length=150, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]