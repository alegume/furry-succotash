# Generated by Django 3.0.4 on 2020-03-12 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='create_date',
            new_name='created_date',
        ),
    ]
