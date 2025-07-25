from accounts.models.account.AccountBase import AccountBase


class WalletAccount(AccountBase):
    class Meta:
        verbose_name = "Carteira"
        verbose_name_plural = "Carteiras"

    def save(self, *args, **kwargs):
        self.account_type = "WALLET"
        super().save(*args, **kwargs)
