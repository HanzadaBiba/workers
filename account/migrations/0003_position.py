# Generated by Django 2.2 on 2019-05-22 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20190522_1610'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Должнотость')),
            ],
            options={
                'verbose_name': 'Должность',
                'verbose_name_plural': 'Должность',
            },
        ),
    ]
