# Generated by Django 3.1.2 on 2020-10-16 11:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0003_auto_20201013_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='password123',
            field=models.CharField(default=django.utils.timezone.now, max_length=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='username',
            field=models.CharField(default=django.utils.timezone.now, max_length=8),
            preserve_default=False,
        ),
    ]