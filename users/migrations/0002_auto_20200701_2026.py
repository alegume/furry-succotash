# Generated by Django 3.0.6 on 2020-07-01 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='birth_date',
            field=models.DateField(help_text='Use o formato dd/mm/AAAA', null=True, verbose_name='Data de nascimento'),
        ),
    ]
