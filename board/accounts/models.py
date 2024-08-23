from django.db import models
from django.contrib.auth.models import User


class Authors(models.Model):
    authorUsers = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.authorUsers.username.title()
