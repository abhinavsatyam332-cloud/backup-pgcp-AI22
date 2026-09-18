from Account import  Account
from Exceptions import (AccountNotFound, DepositMoneyError, WithdrawError)


class CurrentAccount(Account):
    def __init__(self, id, name, balance):
        super().__init__(id, name, balance)

    def __str__(self):
        return f'id:{self._acc_id}, Name: {self._name}, Balance: {self._balance}'

    def withdraw(self, amount: int):
        if self.balance - amount < 10000:
            raise WithdrawError

        self.balance = self.balance - amount

        return f'Rs.{amount} withdraw successfull.. Remaining balance is Rs.{self._balance}'

    def deposit(self, amount: int):
        if amount <= 2_00_000:
            self.balance = self.balance + amount

            return f"Rs.{amount} deposited successfully.. new balance is Rs.{self._balance}"


        else:
            raise DepositMoneyError("max limit is Rs. 2,00,000 ")

