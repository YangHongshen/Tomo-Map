# Generated by Django 3.0.3 on 2020-06-07 02:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mapApp', '0008_auto_20200607_0208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendlist',
            name='friend',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]