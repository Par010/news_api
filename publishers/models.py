from django.db import models

# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Publisher'
        verbose_name_plural = 'Publishers'

    def __str__(self):
        return "{0}-{1}".format(self.id, self.name)
