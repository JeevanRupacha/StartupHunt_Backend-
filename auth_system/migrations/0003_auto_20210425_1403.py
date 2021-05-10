# Generated by Django 3.1.7 on 2021-04-25 08:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth_system', '0002_useraccount_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='profile_image',
        ),
        migrations.AddField(
            model_name='useraccount',
            name='profile_image_url',
            field=models.URLField(default=django.utils.timezone.now, max_length=500, verbose_name=' Profile image '),
            preserve_default=False,
        ),
    ]