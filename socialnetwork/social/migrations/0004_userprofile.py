# Generated by Django 4.0.3 on 2023-01-06 15:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('social', '0003_rename_body_comment_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='user')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('bio', models.TextField(blank=True, max_length=500, null=True)),
                ('birth_date', models.DateTimeField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('picture', models.ImageField(blank=True, default='upload/profile_pictures/default.png', upload_to='upload/profile_pictures')),
            ],
        ),
    ]