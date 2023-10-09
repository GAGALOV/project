# Generated by Django 3.2.20 on 2023-10-03 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('figma', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(to='figma.Category'),
        ),
    ]
