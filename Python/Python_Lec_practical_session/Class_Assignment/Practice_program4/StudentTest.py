from StudentManagement import StudentManagement

mgmt = StudentManagement()
mgmt.addData(1,"ram",{"math":70, "english":90, "java": 70})
mgmt.addData(2,"anil",{"math":100, "english":90, "java": 70})
mgmt.addData(3,"ramesh",{"math":92, "english":97, "java": 70})
mgmt.addData(4,"sham",{"math":27, "english":92, "java": 70})


print(f'\n\nstudent id 4 =   {mgmt.searchById(4)}')

print("\n\n")
mgmt.displayData()


print("\n\n")
print(f'GPA for {mgmt.giveGpaFor(3)}')

print("\n\n")
mgmt.sortByName()
mgmt.displayData()