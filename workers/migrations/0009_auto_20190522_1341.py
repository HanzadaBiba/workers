# Generated by Django 2.2 on 2019-05-22 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0008_auto_20190522_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workers',
            name='status',
            field=models.CharField(choices=[('На работе', 'work'), ('В отпуске', 'В отпуске'), ('В командировке', 'В командировке'), ('В Больничном', 'В Больничном')], max_length=15, verbose_name='Статус'),
        ),
    ]
