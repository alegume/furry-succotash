# Generated by Django 3.0.4 on 2020-04-17 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20200417_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.BigIntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='PostLike',
        ),
    ]