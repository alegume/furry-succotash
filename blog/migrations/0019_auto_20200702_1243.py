# Generated by Django 3.0.6 on 2020-07-02 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20200417_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='attachment',
            field=models.FileField(blank=True, default=None, upload_to=''),
        ),
        migrations.AddField(
            model_name='post',
            name='cover',
            field=models.ImageField(blank=True, default=None, upload_to=''),
        ),
    ]
