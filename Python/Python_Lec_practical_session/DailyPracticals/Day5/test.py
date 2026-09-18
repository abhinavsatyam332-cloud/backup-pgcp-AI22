
from EmployeePortal import (SalariedEmployee,ContractEmployee,Manager)
from Payroll import Payroll
from consultant import consultant


se = SalariedEmployee(1,"ram",20000,"QWERT435")
Payroll.add_employee(se)
print(se)
print(se.calc_net())
print(se.calculate_gross())

ce = ContractEmployee(80,"shyam",10,435)
Payroll.add_employee(ce)
print(ce)
print(ce.calculate_gross())



mg = Manager(5,"fdg",34543,10,"dg")
Payroll.add_employee(mg)
print(mg)
print(mg.calculate_gross())
print(mg.calc_net())


c = consultant("dfg")
Payroll.display_tax(c)