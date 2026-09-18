from Transaction import Transaction
from SavingsAccount import SavingsAccount
from CurrentAccount import CurrentAccount
from Exceptions import (AccountNotFound, DepositMoneyError, WithdrawError)


account = []

# ac1 = SavingsAccount(1,"ram",90000,"corporate")
# ac2 = CurrentAccount(2,"sham",2000)
#
# print(ac1)
# print(ac2)
# Transaction.withdraw_from_account(ac1,90000)
# Transaction.deposit_to_account(ac2,700)
# print(ac1)
# print(ac2)


while(True):
    print("\n\n---- Bank Account System ----\n")
    print("1 -> Create Savings Account")
    print("2 -> Create Current Account")
    print("3 -> Deposit ")
    print("4 -> Withdraw ")
    print("5 -> Exit ")
    print("6 -> Show all accounts \n")
    print("------------------------------")
    n = int(input("\nEnter your option: "))

    try:
        match n:
            case 1:

                id = int(input("\nEnter id: "))
                name = input("Enter name: ")
                amt = int(input("Enter ammount to deposit "))
                typeno = int(input("Enter type as 1 -> personel / 2 -> corporate "))

                type = ''
                if typeno == 1:
                    type = 'personel'
                else:
                    type = 'corporate'

                acc = SavingsAccount(id,name,amt,type)
                account.append(acc)
                print("\nAccount created successfully..")
            case 2:
                id = int(input("\nEnter id: "))
                name = input("Enter name: ")
                amt = int(input("Enter ammount to deposit "))

                acc = CurrentAccount(id, name, amt)
                account.append(acc)
                print("\nAccount created successfully..")
            case 3:
                idf = int(input("\nEnter id of account to deposit: "))
                accounttt = None
                for acc in account:
                    if acc.acc_id == idf:
                        accounttt =acc
                        break
                if accounttt == None:
                    raise AccountNotFound("\nAccount not found")
                else:
                    amt = int(input("\nEnter amount to deposit: "))

                    Transaction.deposit_to_account(accounttt, amt)

            case 4:
                idf = int(input("\nEnter id of account to withdraw from: "))
                accounttt = None
                for acc in account:
                    if acc.acc_id == idf:
                        accounttt = acc
                        break
                if accounttt == None:
                    raise AccountNotFound("Account not found")
                else:
                    amt = int(input("\nEnter amount to withdraw: "))

                    Transaction.withdraw_from_account(accounttt, amt)
            case 5:
                break
            case 6:
                print("\n--- Account In System ---")
                for acc in account:
                    print(acc)
                print("_________________________")

            case _:
                print("Please enter valid choice")

    except AccountNotFound as e:
        print(e)
    except DepositMoneyError as e:
        print(e)
    except WithdrawError as e:
        print(e)
