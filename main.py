class Student:
    def __init__(self, id, name, school, _class, score):
        self.id = id
        self.name = name
        self.school = school
        self._class = _class
        self.score = score


f = open('students.txt', 'r', encoding='utf-8')
f.readline()
students = []
for i in f:
    students.append(Student(*i.strip().split(',')))

for i in range(len(students)):
    if students[i].score == 'None':
        students[i].score = -1
    else:
        students[i].score = int(students[i].score)

for i in range(1, len(students)):
    j = i-1
    sortingStudent = students[i]
    while j >= 0 and sortingStudent.score > students[j].score:
        students[j+1] = students[j]
        j -= 1
    students[j + 1] = sortingStudent

for i in range(len(students)):
    if students[i].score == -1: students[i].score = 'None'

for i in range(1, 4):
    print(f"{i} место: {students[i-1].name}")