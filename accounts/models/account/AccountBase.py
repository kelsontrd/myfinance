from django.db import models
from accounts.models.shared.TimesTump import Timestamp
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User


class AccountBase(Timestamp):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuário")
    name = models.CharField(max_length=255, verbose_name="Nome da Conta")
    balance = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        default=0.00,
        verbose_name="Saldo",
    )
    observations = models.TextField(
        max_length=200, blank=True, null=True, verbose_name="Observações"  # Adicionar
    )

    @property
    def account_type_display(self):
        return self._meta.verbose_name

    def get_balance_display(self):
        return f"R$ {self.balance:,.2f}"

    class Meta:
        abstract = True
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} ({self.get_account_type_display()})"
