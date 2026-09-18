
from Student import Student

class StudentManagement:

    def __init__(self):
        self._studentList = []

    def addData(self, rollNo, studentName, marks):
        s1 = Student(rollNo, studentName, marks)
        self._studentList.append(s1)
        print(f'{studentName} added in system')

    def displayData(self):
        for student in self._studentList:
            print(f'Id: {student.id}, RollNo: {student.rollNo}, Name: {student.studentName}, Marks: {student.marks}')

    def searchById(self,id):
        s = None
        for student in self._studentList:
            if student.id == id:
                s = student
                break
        return s

    def sortByName(self):
        self._studentList = list(sorted(self._studentList, key = lambda student: student.studentName   ))

    def giveGpaFor(self, id):
        stud = self.searchById(id)
        return f'{stud.calculate_gpa():.02f}'
