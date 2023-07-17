from django.db import models


class Species(models.Model):
    title = models.CharField(max_length=100, verbose_name='название породы')
    description = models.TextField(verbose_name='описание')
