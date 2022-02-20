from django.db import models


class Hacker(models.Model):
    nickname = models.CharField(max_length=50)

    def __str__(self):
        return self.nickname


class Speech(models.Model):
    speech = models.TextField(max_length=100000)



