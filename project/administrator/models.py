from django.db import models


class Administrator(models.Model):
    id_administrator = models.AutoField(primary_key=True, verbose_name='id_administrator')
    name = models.CharField(max_length=500)
    email = models.EmailField(max_length=300)
    birth_date = models.DateField()
    active = models.BooleanField()

    class Meta:
        db_table = 'administrator'

    def __repr__(self):
        return f"{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
