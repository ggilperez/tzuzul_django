# Generated by Django 3.2.9 on 2021-12-10 22:42

from django.db import migrations
import s3direct.fields


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_usuario_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='curriculum',
            field=s3direct.fields.S3DirectField(blank=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='facturas',
            field=s3direct.fields.S3DirectField(blank=True),
        ),
    ]
