from django.db import models


# Create your models here.


class Language(models.Model):
    name = models.CharField(max_length=100, verbose_name="Язык")

    def __str__(self):
        return self.name

    class Meta:
        ''' Model settings '''
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'
        ordering = ['name']


class Bedroom(models.Model):
    language = models.ForeignKey('Language', on_delete=models.PROTECT, null=True, verbose_name="Язык")
    description = models.TextField(verbose_name="Описание")
    keywords = models.CharField(max_length=255, blank=True, verbose_name="Ключевые слова")

    class Meta:
        ''' Model settings '''
        verbose_name = 'Спальня'
        verbose_name_plural = 'Спальни'
