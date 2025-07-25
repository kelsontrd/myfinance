from django.db import models
from accounts.models.account.AccountBase import AccountBase


class InvestmentAccount(AccountBase):
    INTEREST_CHOICES = [
        ("FIXED", "Renda Fixa"),
        ("VARIABLE", "Renda Variável"),
    ]

    interest_type = models.CharField(
        max_length=10,
        choices=INTEREST_CHOICES,
        default="FIXED",
        verbose_name="Tipo de Investimento",
    )
    expected_return = models.DecimalField(
        max_digits=5, decimal_places=2, default=0.0, verbose_name="Retorno Esperado (%)"
    )

    class Meta:
        verbose_name = "Conta de Investimento"
        verbose_name_plural = "Contas de Investimento"

    def save(self, *args, **kwargs):
        self.account_type = "INVESTMENT"
        super().save(*args, **kwargs)
