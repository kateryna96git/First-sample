from django.db import models

class Screenlist(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50, blank=True, default='')

    class Meta:
        ordering = ['created']