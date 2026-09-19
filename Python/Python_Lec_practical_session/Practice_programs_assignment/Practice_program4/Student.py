from itertools import count
'''
Q1. Create a class 'Student' with roll no, studentName, dictionary/ list of marks(subjectName -> marks[3] / marks[3

 provide following functionalities
A. initiaizer
B. implement __str__ method
C. print student data for given id
D. calculate GPA()
   gpa = (1/3)*m1 + (1/2)*m2 + (1/4)*m3


Q2. Create 5 student objects and store them in a list

For the student data stored in the list perform following operation
1.display all student
2.search by id
3.sort by name
4.calculate GPA of a student

'''





class Student:

    counter = 1
    __ccc = 0

    def __init__(self,rollNo, studentName, marks:dict):
        self._rollNo = rollNo
        self._studentName = studentName
        self._marks = marks
        self._id = Student.counter
        Student.counter +=1
        # Student.id+=1

    def getDataById(self,gid):
        return self._rollNo , self._studentName , self._marks

    def __str__(self):
        return f'Name: {self._studentName}, Roll No: {self._rollNo}, Marks: {self._marks}'

    def __repr__(self):
        return f'Student({repr(self._rollNo)},{repr(self._studentName)}, {repr(self._marks)})'

    def calculate_gpa(self):
        m1,m2,m3 = self._marks.values()
        return (1/3)*m1  + (1/2)*m2 + (1/4)*m3

    @property
    def id(self):
        return self._id

    @property
    def rollNo(self):
        return self._rollNo

    @rollNo.setter
    def rollNo(self,n):
        self._rollNo = n


    @property
    def studentName(self):
        return self._studentName

    @studentName.setter
    def studentName(self, n):
        self._rollNo = n


    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, m):
        self._marks = m

    @id.setter
    def id(self, value):
        self._id = value


