from django.db import models
from accounts.models.shared.TimesTump import Timestamp
from django.contrib.auth.models import User

class Account(Timestamp):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    name = models.CharField(max_length=255, verbose_name='Nome da Conta')
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name='Saldo')

    def __str__(self):
        return f"{self.name} - {self.balance}"

    class Meta:
        verbose_name = 'Conta'
        verbose_name_plural = 'Contas'