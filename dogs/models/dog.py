
from django.db import models


class Dog(models.Model):
    name = models.CharField(max_length=100, verbose_name='имя')
    species = models.ForeignKey('Species', on_delete=models.SET_NULL, null=True, verbose_name='порода')
    birthday = models.DateField(null=True, verbose_name='день рождения')
    photo = models.ImageField(upload_to='dogs/', null=True, blank=False)
