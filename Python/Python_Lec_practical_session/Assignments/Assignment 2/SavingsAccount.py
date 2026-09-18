from abc import ABC
from typing import override
from Exceptions import (AccountNotFound, DepositMoneyError, WithdrawError)

from Account import Account

class SavingsAccount(Account):
    def __init__(self,id,name,balance, type:str):
        super().__init__(id,name,balance)
        self._type =  type
    def __str__(self):
        return f'id:{self._acc_id}, Name: {self._name}, Balance: {self._balance}, Type: {self._type}'

    def withdraw(self, amount: int):
        if self.balance - amount <0:
            raise WithdrawError

        if self._type == 'corporate':
            self.balance = self.balance - amount

            return f'Rs.{amount} withdraw successfull.. Remaining balance is Rs.{self.balance}'
        elif self._balance - amount <= 5000:
            raise WithdrawError
        else:
            self.balance = self.balance - amount

    def deposit(self, amount: int):
        if amount <= 1_00_000:

            self.balance = self.balance + amount

            return f"Rs.{amount} deposited successfully.. new balance is Rs.{self.balance}"

        else:
            raise DepositMoneyError("max limit is Rs. 1,00,000 ")
