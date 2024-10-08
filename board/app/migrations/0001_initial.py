# Generated by Django 5.1 on 2024-08-20 12:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameCat', models.CharField(choices=[('Tanks', 'Танки'), ('Healers', 'Хилы'), ('Damage Dealer', 'ДД'), ('Vendors', 'Торговцы'), ('GuildMasters', 'Гилдмастеры'), ('QuestGivers', 'Квестгиверы'), ('Blacksmiths', 'Кузнецы'), ('Tanners', 'Кожевники'), ('PotionMakers', 'Зельевары'), ('SpellMasters', 'Мастера заклинаний')], default='Tanks', max_length=64, verbose_name='Category')),
                ('title', models.CharField(max_length=128)),
                ('text', models.TextField()),
                ('files', models.FileField(blank=True, upload_to='uploads/')),
                ('dateMsg', models.DateTimeField(auto_now_add=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('dateComm', models.DateTimeField(auto_now_add=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.message')),
            ],
        ),
    ]
