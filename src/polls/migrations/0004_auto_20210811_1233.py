# Generated by Django 3.2.5 on 2021-08-11 12:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20210811_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='choice',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]