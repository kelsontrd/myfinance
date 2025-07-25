from django.core.exceptions import ValidationError
from django.db import models
from accounts.models.account.AccountBase import AccountBase


class CheckingAccount(AccountBase):
    overdraft_limit = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        verbose_name="Limite de Cheque Especial",
    )

    # Validação customizada sem MinValueValidator
    def clean(self):
        super().clean()
        if self.balance < -self.overdraft_limit:
            raise ValidationError("Saldo não pode exceder o limite do cheque especial")

    class Meta:
        verbose_name = "Conta Corrente"
        verbose_name_plural = "Contas Correntes"

    def save(self, *args, **kwargs):
        self.account_type = "CHECKING"
        super().save(*args, **kwargs)
