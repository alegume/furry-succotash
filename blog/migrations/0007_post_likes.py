# Generated by Django 3.0.4 on 2020-04-16 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.BigIntegerField(default=0),
        ),
    ]
