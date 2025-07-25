# accounts/factories.py
from accounts.models.account.WalletAccount import WalletAccount
from accounts.models.account.ChekingAccount import CheckingAccount
class AccountFactory:
    @staticmethod
    def create_default_wallet(user):
        return WalletAccount.objects.create(
            user=user,
            name="Carteira Principal",
            balance=0.00
        )
    
    @staticmethod
    def create_checking_with_overdraft(user, name, overdraft_limit):
        return CheckingAccount.objects.create(
            user=user,
            name=name,
            overdraft_limit=overdraft_limit
        )