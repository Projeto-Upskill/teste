from django.db import models


class Client(models.Model):
    id_client = models.IntegerField(primary_key=True, verbose_name='id_client')
    name = models.CharField(max_length=500)

    class Meta:
        __name__ = "client"
