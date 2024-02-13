class Student:
    def __init__(self, id, name, titleProject_id, _class, score):
        self.id = int(id)
        self.name = name
        self.titleProject_id = int(titleProject_id)
        self._class = _class
        if score == 'None':
            self.score = 0
        else:
            self.score = int(score)

def projectInfo(students, id):
    for student in students:
        if student.titleProject_id == id:
            print(f"Проект №{id}:\nУченик: {student.name}.\nКласс: {student._class}.\nОценка за проект: {student.score}.")
            break

f = open('students.txt', 'r', encoding='utf-8')
f.readline()
students = []
for i in f:
    students.append(Student(*i.strip().split(',')))

for i in range(1, len(students)):
    j = i-1
    sortingStudent = students[i]
    while j >= 0 and sortingStudent.score > students[j].score:
        students[j+1] = students[j]
        j -= 1
    students[j + 1] = sortingStudent

for i in range(1, 4):
    print(f"{i} место: {students[i-1].name}")

print()
projectInfo(students, 304)
