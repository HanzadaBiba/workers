# Generated by Django 2.2 on 2019-05-22 05:45

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0005_auto_20190521_1628'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='workers',
            managers=[
                ('worked', django.db.models.manager.Manager()),
            ],
        ),
    ]
