'''

Q.5
1. Find employees that know 'python'
2. Add a new skill - 'test' in skillset of all employees
3. Sort employees by skills
for the given dictionary of employees

'''

from pprint import pprint

employees = [
    {"Name": "ram", "salary": 10000, "age": 20, "languages": ["c", "python"], "skill": ["communication"]},
    {"Name": "priya", "salary": 45000, "age": 32, "languages": ["java", "cpp", "python"], "skill": ["leadership", "problem-solving"]},
    {"Name": "amit", "salary": 25000, "age": 25, "languages": ["c"], "skill": ["teamwork"]},
    {"Name": "neha", "salary": 60000, "age": 41, "languages": ["java", "python"], "skill": ["negotiation", "conflict resolution"]},
    {"Name": "rajesh", "salary": 15000, "age": 22, "languages": ["cpp"], "skill": ["adaptability"]},
    {"Name": "satyam", "salary": 95000, "age": 35, "languages": ["java", "c", "cpp"], "skill": ["project management", "leadership"]},
    {"Name": "vikram", "salary": 35000, "age": 28, "languages": ["python", "c"], "skill": ["critical thinking"]},
    {"Name": "pooja", "salary": 20000, "age": 24, "languages": ["java"], "skill": ["creativity", "communication"]},
    {"Name": "abhinav", "salary": 95000, "age": 45, "languages": ["python", "cpp", "java", "c"], "skill": ["strategic planning", "public speaking"]},
    {"Name": "ananya", "salary": 50000, "age": 29, "languages": ["cpp", "python"], "skill": ["time management"]}
]
print("\n --------------------------------------------------------- \n\n")

print("Employees whos knows python \n")
employees_who_knows_python =  list(filter(lambda  emp: 'python' in emp['languages'], employees))
pprint(employees_who_knows_python , width=200)


print("\n --------------------------------------------------------- \n\n")
for emp in employees:
    emp['skill'].append('test')
print("Employees with added test in skill \n")
pprint(employees , width=200)

print("\n --------------------------------------------------------- \n\n")

print("Employees with sorting by skill length")
sorted_emp_by_skill_len =  sorted(employees ,key=lambda emp: len(emp['skill']))
pprint(sorted_emp_by_skill_len , width = 200)

print("\n --------------------------------------------------------- \n\n")

print("Employees whos knows python \n")

emp_data = {'Amol': ['C', 'C++', 'Java'], 'Aditya': ['Angular', 'Java','python'],
            'Aditi': ['Python', 'PHP', 'Database']}
emps_py =  [name for name , lang in emp_data.items() if 'python' in lang]
pprint(emps_py)


