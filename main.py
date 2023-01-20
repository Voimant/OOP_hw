
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def _aver_grade(self):
        list_grade = []
        for v in self.grades.values():
            for list_gr in v:
                list_grade.append(list_gr)
        summ_lst = sum(list_grade)
        aver_grade = round(summ_lst / len(list_grade), 1)
        return aver_grade

    def __str__(self):
        output = (f'Студент:\n'
                  f'Имя: {self.name}\n'
                  f'Фамилия: {self.surname}\n'
                  f'Средняя оценка за домашнее задание: {self._aver_grade()}\n'
                  f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                  f'Завершенные курсы: {", ".join(self.finished_courses)}')
        return output

    def rate_lector(self, lector, course, grade):
        if isinstance(lector, Lector) or course in self.finished_courses or course in lector.courses_attached:
            if course in lector.grades:
                lector.grades[course] += [grade]
                return lector.grades
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if self._aver_grade() > other._aver_grade():
            print(f'{self.name} имеет больший бал чем {other.name}')
        else:
            print(f'{other.name} имеет больший бал чем {self.name}')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lector(Mentor):
    def __init__(self, name, surname, courses_attached):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def _aver_grade(self):
        list_grade = []
        for v in self.grades.values():
            for list_gr in v:
                list_grade.append(list_gr)

        summ_lst = sum(list_grade)
        aver_grade = round(summ_lst / len(list_grade), 1)
        return aver_grade

    # Метод сравнения для лекторов, такой же в студентах
    def __lt__(self, other):
        if self._aver_grade() > other._aver_grade():
            print(f'{self.name} имеет больший бал чем {other.name}')
        else:
            print(f'{other.name} имеет больший бал чем {self.name}')

    def __str__(self):
        output_lec = (f'Лектор:\n'
                      f'имя: {self.name}\nФамилия: {self.surname}'
                      f'\nСредняя оценка за лекции: {self._aver_grade()}')
        return output_lec


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        output_print = (f'Проверяющий:\nИмя: {self.name}\nФамилия: {self.surname}')
        return output_print


def avage_lector(lector_lst, course):
    grade_list = []
    for lector in lector_lst:
        for k, v in lector.grades.items():
            if k in course:
                grade_list.append(v)
            else:
                continue
    list_gen = [lst for list in grade_list
                for lst in list]
    final_grade = sum(list_gen) / len(list_gen)
    print(f'Средняя оценка лекторов по курусу {course} : {final_grade}')


def avage_student(stud_lst, course):
    grade_list = []
    for students in stud_lst:
        for k, v in students.grades.items():
            if k in course:
                grade_list.append(v)
            else:
                continue
    list_gen = [lst for list in grade_list
                for lst in list]
    final_grade = sum(list_gen) / len(list_gen)
    print(f'Средняя оценка студентов по курусу {course} : {final_grade}')


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Assembler']
best_student.finished_courses += ['C+']

cool_student = Student("Sara", "Conor", "famale")
cool_student.courses_in_progress += ["Python"]

a_student = Student('Artur', 'Kairatov', 'male')
a_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['C+']

cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 5)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'C+', 6)

cool_reviewer.rate_hw(a_student, 'Python', 3)
cool_reviewer.rate_hw(a_student, 'Python', 2)
cool_reviewer.rate_hw(a_student, 'Python', 1)

cool_reviewer.rate_hw(cool_student, 'Python', 10)
cool_reviewer.rate_hw(cool_student, 'Python', 9)
cool_reviewer.rate_hw(cool_student, 'Python', 8)

cool_lector = Lector("Oleg", "Buligin", "Python")
cool_lector.courses_attached += ["Python"]
cool_lector.courses_attached += ["C+"]
cool_lector.courses_attached += ['Assembler']

test_lector = Lector("Вася", 'Пупкин', "Python")
test_lector.courses_attached += ["Python"]
test_lector.courses_attached += ["C+"]
test_lector.courses_attached += ['Assembler']

best_student.rate_lector(cool_lector, "Python", 10)
best_student.rate_lector(cool_lector, "Python", 8)
best_student.rate_lector(cool_lector, "Python", 9)

cool_student.rate_lector(test_lector, "Python", 10)
cool_student.rate_lector(test_lector, "Python", 10)
cool_student.rate_lector(test_lector, "Python", 10)

cool_student.rate_lector(test_lector, "C+", 10)

cool_student.rate_lector(cool_lector, "C+", 10)

stud_list = [cool_student, a_student]
lector_list = [cool_lector, test_lector]

print("оценки выставленные лекторам")
print(test_lector.grades)
print(cool_lector.grades)
print("---------------")
print("оценки выставленные студентам")
print(cool_student.grades)
print(best_student.grades)
print("--------------------")
print(cool_lector.__str__())
print("--------------------")
print(best_student.__str__())
print('----------------')
print(a_student.__str__())
print('----------------')
print(cool_reviewer.__str__())
print("------------------")
best_student > a_student
cool_lector > test_lector

print("-------------")
avage_student(stud_list, 'Python')
avage_lector(lector_list, 'Python')