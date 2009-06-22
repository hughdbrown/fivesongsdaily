import logging

from django.db import models
from django.utils.translation import ugettext_lazy as _

class Message(models.Model):
    message = models.TextField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return u"%s" %self.message

    class Meta:
        ordering = ['-created_at']

