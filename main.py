class Student:
    def __init__(self, id, name, school, _class, score):
        self.id = id
        self.name = name
        self.school = school
        self._class = _class
        self.score = score


f = open('students.txt', 'r')
f.readline()
students = []
for i in f:
    students.append(Student(*i.split(',')))

for i in range(len(students)):
    pass