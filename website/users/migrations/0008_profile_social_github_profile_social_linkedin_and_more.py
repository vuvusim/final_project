# Generated by Django 4.1.3 on 2022-12-08 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_profile_social_github_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='social_github',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='social_linkedin',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='social_twitter',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='social_website',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='social_youtube',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
