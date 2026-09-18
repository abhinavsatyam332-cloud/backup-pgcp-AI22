from abc import ABC, abstractmethod
from typing import override

from DailyPracticals.Day5.consultant import consultant

class Employee(ABC):        # ABC is compulsory to make class abstract
    def __init__(self, emp_id, name):
        self._emp_id = emp_id
        self._name = name

    @property
    def emp_id(self):
        return self._emp_id

    @property
    def name(self):
        return self._name

    @abstractmethod          # this decorator make the method abstract
    def calculate_gross(self):
        pass

    def __str__(self):
        return f'Employee Data  ID: {self._emp_id}, Name:{self._name}'


class SalariedEmployee(Employee, consultant):
    def __init__(self, emp_id, name, basic,pan):
        # super().__init__(emp_id, name)
        consultant.__init__(self,pan)
        Employee.__init__(self,emp_id, name)
        self._basic = basic

    @property
    def basic(self):
        return self._basic

    @override
    def calculate_gross(self):
        hra = self._basic * 0.4
        da = self._basic * 0.15
        return self._basic+hra+da

    def calc_net(self):
        gross = self.calculate_gross()
        tax = gross * 0.1
        return gross - tax

    def __str__(self):
        return f'Salaried Employee Data   ---- ID: {self._emp_id}, Name:{self._name}, Pan: {self._pan}, Basic:{self._basic}, Gross Salary: {self.calculate_gross()}, Calculate Net: {self.calc_net()} '



class ContractEmployee(Employee):
    def __init__(self, emp_id, name ,rate,hour):
        super().__init__(emp_id, name)

        self._rate = rate
        self._hour = hour

    @property
    def rate(self):
        return self._rate

    @property
    def hour(self):
        return self._hour
    def __str__(self):
        return f'Contract Employee Data   ---- ID: {self._emp_id}, Name:{self._name}, Gross Salary: {self.calculate_gross()}, Rate: {self.rate}, hour: {self.hour} '


    @override
    def calculate_gross(self):
        return self._rate * self._hour


class Manager(SalariedEmployee):

    def __init__(self, emp_id,name,basic,allowance,pan):
        super().__init__(emp_id, name,basic,pan)
        self._allowance = allowance

    @property
    def allowance(self):
        return self._allowance

    @override
    def calculate_gross(self):
        hra = self._basic * 0.5
        da = self._basic * 0.15
        return hra + da + self._allowance

    @override
    def calc_net(self):
        gross = self.calculate_gross()
        tax = gross * 0.1
        return gross - tax

    def __str__(self):
        return f'Manager Employee Data   ---- ID: {self._emp_id}, Name:{self._name}, Pan: {self._pan}, Basic:{self._basic}, Allowance: {self._allowance}, Gross Salary: {self.calculate_gross()}, Calculate Net: {self.calc_net()} '





