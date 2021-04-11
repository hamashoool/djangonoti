from django.contrib.auth.models import User
from django.db import models

cascade = models.CASCADE


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=cascade)
    message = models.CharField(max_length=1000, blank=True, null=True)
    verb = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'noti for {self.user}'
