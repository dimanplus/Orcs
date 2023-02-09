from django.db import models
from django.urls import reverse

# Create your models here.

class Orc(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Звание")
    content = models.TextField(blank=True, verbose_name="Описание")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    der = models.ManyToManyField('Der', related_name='der', verbose_name="Деревня")

    def save(self, *args, **kwargs):
        self.title = self.title.lower()
        self.content = self.content.lower()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Орки в деревне'
        verbose_name_plural = 'Орки в деревне'

class Der(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Деревни'
        verbose_name_plural = 'Деревни'