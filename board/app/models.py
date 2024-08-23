from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Message(models.Model):
    TYPE = (
        ('Tanks', 'Танки'),
        ('Healers', 'Хилы'),
        ('Damage Dealer', 'ДД'),
        ('Vendors', 'Торговцы'),
        ('GuildMasters', 'Гилдмастеры'),
        ('QuestGivers', 'Квестгиверы'),
        ('Blacksmiths', 'Кузнецы'),
        ('Tanners', 'Кожевники'),
        ('PotionMakers', 'Зельевары'),
        ('SpellMasters', 'Мастера заклинаний'),
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    nameCat = models.CharField(max_length=64, unique=False, choices=TYPE, verbose_name='Category', default='Tanks')
    title = models.CharField(max_length=128)
    text = models.TextField()
    files = models.FileField(upload_to='uploads/', blank=True)
    dateMsg = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title.title()

    def get_absolute_url(self):
        return reverse('Messages')


class Comment(models.Model):
    author = models.ForeignKey(User, unique=False, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, unique=False, on_delete=models.CASCADE)
    text = models.TextField()
    status = models.BooleanField(default=False)
    dateComm = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.author}:{self.message}:{self.text[:10]}'

    def get_absolute_url(self):
        return reverse('Comments', args=[str(self.message.id)])
