from django.contrib import admin
from accounts.models.account.Account import Account
from accounts.models.account.AccountType import AccountType

admin.site.register(Account)
admin.site.register(AccountType)