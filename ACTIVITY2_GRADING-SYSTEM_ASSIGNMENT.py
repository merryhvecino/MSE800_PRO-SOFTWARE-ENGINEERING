class Student_Grade:
    
    def __init__(self):
        self.grade = {}

    def add_grade(self, name, grade):
        self.grade[name] = grade
    
    def show_grades(self):
        print(f'/nStudent Grades:')
        for name, grade in self.grade.items():
            print(f'{name}: {grade}')
            
students = Student_Grade()

for i in range(3):
    name = input(f'Enter Student Name: ')
    grade = input(f'Enter Grade for {name}: ')
    students.add_grade(name, grade)
    
students.show_grades()
    
    