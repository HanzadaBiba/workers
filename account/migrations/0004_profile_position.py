# Generated by Django 2.2 on 2019-05-22 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='position',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='account.Position', verbose_name='Должность'),
            preserve_default=False,
        ),
    ]
