# Generated by Django 3.0.4 on 2020-04-16 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200416_1635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='post',
            name='views',
        ),
        migrations.DeleteModel(
            name='PostLike',
        ),
    ]
