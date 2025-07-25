from django.contrib import admin

from accounts.models.account.InvestimentAccount import InvestmentAccount
from accounts.models.account.ChekingAccount import CheckingAccount
from accounts.models.account.SavingAccount import SavingsAccount
from accounts.models.account.WalletAccount import WalletAccount

admin.site.register(InvestmentAccount)
admin.site.register(CheckingAccount)
admin.site.register(SavingsAccount)
admin.site.register(WalletAccount)
