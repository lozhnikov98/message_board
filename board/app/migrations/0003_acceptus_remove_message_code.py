# Generated by Django 5.1 on 2024-08-22 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_message_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='acceptUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.SmallIntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='message',
            name='code',
        ),
    ]
