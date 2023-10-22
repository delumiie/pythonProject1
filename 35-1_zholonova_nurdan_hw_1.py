class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        return f'FULL NAME: {self.fullname}, AGE: {self.age}, MARRIAGE: {self.is_married} '


class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def introduce_myself(self):
        info1 = super().introduce_myself()
        return f'STUDENT: \n{info1} \nGPA: {self.average_marks()}'

    def average_marks(self):
        average = sum(self.marks.values()) / len(self.marks.values())
        return average


def create_students():
    student_1 = Student('Tsoy Alina', 17, False, {'math': 3, 'russian': 5, 'physics': 4})
    student_2 = Student('Akjolova Ayana', 17, False, {'math': 5, 'russian': 5, 'physics': 5})
    student_3 = Student('Sadykova Gulhava', 15, False, {'math': 4, 'russian': 5, 'physics': 3})
    students = [student_1, student_2, student_3]
    return students


class Teacher(Person):
    base_salary = 50000

    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    def get_salary(self):
        if self.experience > 3:
            bonus = round((self.experience - 3) * 0.05 * self.base_salary)
            return self.base_salary + bonus
        else:
            return self.base_salary


teacher = Teacher('Nuriza Shumkarbekova', 32, True, 7)
print(f'TEACHER: \n{teacher.introduce_myself()}')
print(f'SALARY: {teacher.get_salary()}')
create_students()

students_list = create_students()
for student in students_list:
    info = student.introduce_myself()
    print(info)
