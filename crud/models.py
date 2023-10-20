from django.db import models


# Create your models here.
class ClientInfo(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=260)
    phone = models.CharField(max_length=10)
    status = models.BooleanField(default=True)

    class Meta:
        ordering =[ 'name']

    def __str__(self):
        return self.name