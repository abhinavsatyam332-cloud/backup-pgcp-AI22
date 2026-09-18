from Account import Account
from SavingsAccount import Account
from Exceptions import (AccountNotFound, DepositMoneyError, WithdrawError)
from abc import  ABC
from CurrentAccount import Account

class Transaction:

    def withdraw_from_account(account: Account, amount: int):
        account.withdraw(amount)

    def deposit_to_account(account: Account, amount: int):

        account.deposit(amount)

