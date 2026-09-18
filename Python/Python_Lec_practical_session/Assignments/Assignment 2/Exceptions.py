from abc import abstractmethod, ABC


class AccountNotFound(Exception):
    # super().__init__("Account not found for this user")
    pass

class DepositMoneyError(Exception):
    # super().__init__("Cant deposit money: [maximum limit is Rs. 1,00,000]")
    pass

class WithdrawError(Exception):
    # super().__init__("Cant withdraw money: ")
    pass
