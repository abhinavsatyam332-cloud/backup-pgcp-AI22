from abc import abstractmethod
from typing import override

from DailyPracticals.Day5.TaxPayer import TaxPayer
from EmployeePortal import (Employee, SalariedEmployee,ContractEmployee,Manager)


class Payroll:
    all_employees = []

    @staticmethod
    def add_employee( emp:Employee):
        Payroll.all_employees.append(emp)

    @staticmethod
    def display_tax(emp:TaxPayer):
        print(f'Tax: {emp.calculate_tax()}')

    @staticmethod
    def display_gross(e:Employee):
        print(f'Gross sal for month: {e.calculate_gross()}')

    @staticmethod
    def display_net(e:SalariedEmployee):
        print(f'Net salary for the month: {e.calc_net()}')


