from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    keywords = models.CharField(max_length=255, blank=True, verbose_name="Ключевые слова")
    description = models.TextField(verbose_name="Описание")

    class Meta:
        ''' Model settings '''
        verbose_name = 'Спальня'
        verbose_name_plural = 'Спальни'
        ordering = ['id']


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    language = models.ForeignKey('Language', on_delete=models.PROTECT, null=True, verbose_name="Язык")

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()