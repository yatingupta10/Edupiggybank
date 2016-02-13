from django.db import models
from django.utils import timezone


class Passbook(models.Model):
    name = models.ForeignKey('auth.User')
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    transaction = models.IntegerField()

    def __str__(self):
        return self.text 

    

    