import random

class Student:
    def generatePassword(self):
        alph = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        password = ''
        for i in range(8):
            password += random.choice(alph)
        return password
    def generateLogin(self, name):
        FIO = name.split()
        return FIO[0] + '_' + FIO[1][0] + FIO[2][0]
    def __init__(self, id, name, titleProject_id, _class, score):
        self.id = int(id)
        self.name = name
        self.titleProject_id = int(titleProject_id)
        self._class = _class
        if score == 'None':
            self.score = 0
        else:
            self.score = int(score)
        self.login = self.generateLogin(name)
        self.password = self.generatePassword()

def projectInfo(students, id):
    for student in students:
        if student.titleProject_id == id:
            print(f"Проект № {id} делал: {student.name}, он(а) получил(а) оценку - {student.score}.")
            break

fin = open('students.txt', 'r', encoding='utf-8')
fin.readline()
students = []
for i in fin:
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


fout = open('students_password.csv', 'w')
fout.write('id,Name,titleProject_id,class,score,login,password\n')
for student in students:
    fout.write(f'{student.id},{student.name},{student.titleProject_id},{student._class},{student.score},{student.login},{student.password}\n')
fout.close()