from django.db import models
from accounts.models.shared.TimesTump import Timestamp

class AccountType(Timestamp):
    description = models.TextField(blank=True, null=True, verbose_name='Descrição')

    def __str__(self):
        return self.description or "Tipo de Conta"

    class Meta:
        verbose_name = 'Tipo de Conta'
        verbose_name_plural = 'Tipos de Conta'