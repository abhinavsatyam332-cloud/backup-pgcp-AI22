from abc import abstractmethod

class Account:

    def __init__(self,acc_id,name, balance):
        self._acc_id = acc_id
        self._name = name
        self._balance = balance

    @property
    def acc_id(self):
        return self._acc_id

    @acc_id.setter
    def acc_id(self,accid):
        self._acc_id=accid


    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, bal):
        self._balance = bal


    def withdraw(self,amount:int):
        pass

    def deposit(self,amount:int):
        pass
