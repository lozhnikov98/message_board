# Generated by Django 5.1 on 2024-08-22 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authors',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='authors',
            name='password',
            field=models.CharField(blank=True, max_length=16),
        ),
    ]
