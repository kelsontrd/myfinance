from django.db import models
from accounts.models.account.AccountBase import AccountBase


class SavingsAccount(AccountBase):
    interest_rate = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0.5,
        verbose_name="Taxa de Juros Mensal (%)",
    )

    class Meta:
        verbose_name = "Conta Poupança"
        verbose_name_plural = "Contas Poupança"

    def save(self, *args, **kwargs):
        self.account_type = "SAVINGS"
        super().save(*args, **kwargs)
