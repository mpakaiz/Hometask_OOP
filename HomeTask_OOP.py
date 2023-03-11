class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return (f'Имя: {self.name} \n'
                f'Фамилия: {self.surname} \n'
                f'Средняя оценка за домашние задания: '
                f'{(sum(sum(x) for x in self.grades.values())) / sum(len(self.grades[a]) for a in self.grades) :.2f} \n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}')

    def __lt__(self, other):
        if not isinstance(other, Mentor):
            print('Не Ментор!')
            return
        else:
            return (sum(sum(x) for x in self.grades.values())) / sum(len(self.grades[a]) for a in self.grades)\
                < (sum(sum(x) for x in other.grades_st.values()))\
                / sum(len(other.grades_st[a]) for a in other.grades_st)

    def __gt__(self, other):
        if not isinstance(other, Mentor):
            print('Не Ментор!')
            return
        else:
            return (sum(sum(x) for x in self.grades.values())) / sum(len(self.grades[a]) for a in self.grades)\
                > (sum(sum(x) for x in other.grades_st.values()))\
                / sum(len(other.grades_st[a]) for a in other.grades_st)

    def __le__(self, other):
        if not isinstance(other, Mentor):
            print('Не Ментор!')
            return
        else:
            return (sum(sum(x) for x in self.grades.values())) / sum(len(self.grades[a]) for a in self.grades)\
                <= (sum(sum(x) for x in other.grades_st.values()))\
                / sum(len(other.grades_st[a]) for a in other.grades_st)

    def __ge__(self, other):
        if not isinstance(other, Mentor):
            print('Не Ментор!')
            return
        else:
            return (sum(sum(x) for x in self.grades.values())) / sum(len(self.grades[a]) for a in self.grades)\
                >= (sum(sum(x) for x in other.grades_st.values()))\
                / sum(len(other.grades_st[a]) for a in other.grades_st)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_st = {}

    def rate_st(self, mentor, student, course, grade):
        if isinstance(student, Student) and course in mentor.courses_attached:
            if course in mentor.grades_st:
                self.grades_st[course] += [grade]
            else:
                self.grades_st[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        len_grades = sum(len(self.grades_st[a]) for a in self.grades_st)
        return (f'Имя: {self.name} \n'
                f'Фамилия: {self.surname} \n'
                f'Средняя оценка за домашние задания: '
                f'{(sum(sum(x) for x in self.grades_st.values())) / len_grades:.2f}')


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
        return (f'''Имя: {self.name}
Фамилия: {self.surname}''')


best_student = Student('Riu', 'Emani', 'Female')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

super_student = Student('Its', 'Me', 'Man')
super_student.courses_in_progress += ['Python']
super_student.courses_in_progress += ['Git']
super_student.courses_in_progress += ['ToDoBot']

cool_mentor = Reviewer('Mister', 'First')
cool_mentor.courses_attached += ['Python']

another_reviewer = Reviewer('Another', 'Reviewer')
another_reviewer.courses_attached += ['Python']
another_reviewer.courses_attached += ['Git']
another_reviewer.courses_attached += ['ToDoBot']

nice_mentor = Lecturer('First', "Lecturer")
nice_mentor.courses_attached += ['Python']

another_lecturer = Lecturer('Another', 'Lecturer')
another_lecturer.courses_attached += ['Python']
another_lecturer.courses_attached += ['Git']
another_lecturer.courses_attached += ['ToDoBot']

some_reviewer = Reviewer('Some', 'Reviewer')
print(some_reviewer)

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
another_reviewer.rate_hw(best_student, 'Python', 8)
another_reviewer.rate_hw(super_student, 'Python', 10)
another_reviewer.rate_hw(super_student, 'Git', 10)
another_reviewer.rate_hw(super_student, 'ToDoBot', 10)

nice_mentor.rate_st(nice_mentor, best_student, 'Python', 9)
nice_mentor.rate_st(nice_mentor, cool_mentor, 'Python', 9)
nice_mentor.rate_st(nice_mentor, best_student, 'Lol', 9)
nice_mentor.rate_st(nice_mentor, best_student, 'Python', 10)
nice_mentor.rate_st(nice_mentor, best_student, 'Python', 7)
nice_mentor.rate_st(nice_mentor, super_student, 'Python', 8)
nice_mentor.rate_st(nice_mentor, super_student, 'Python', 9)
another_lecturer.rate_st(another_lecturer, best_student, 'Python', 9)
another_lecturer.rate_st(another_lecturer, super_student, 'Git', 10)
another_lecturer.rate_st(another_lecturer, super_student, 'Python', 8)
another_lecturer.rate_st(another_lecturer, super_student, 'ToDoBot', 9)

print(nice_mentor)
print(best_student)
print(f'У первого лектора: {nice_mentor.grades_st}')
print(f'У другого лектора: {another_lecturer.grades_st}')
print(best_student > nice_mentor)
print(nice_mentor > best_student)
print(super_student >= another_lecturer)
print(super_student <= nice_mentor)
print(best_student.grades)

students = [best_student, super_student]
lecturers = [nice_mentor, another_lecturer]


def av_grade_st_course(student, course):
    av_grade = []
    for i in student:
        if course in i.grades.keys():
            av_grade += i.grades.get(course)

    print(f'Средняя оценка студентов за домашние задания на курсе {course}: {sum(av_grade) / len(av_grade) :.2f}')


av_grade_st_course(students, 'Python')


def av_grade_lc_course(lecturer, course):
    av_grade = []
    for i in lecturer:
        if course in i.grades_st.keys():
            av_grade += i.grades_st.get(course)

    print(f'Средняя оценка лекторов за лекции на курсе {course}: {sum(av_grade) / len(av_grade) :.2f}')


av_grade_lc_course(lecturers, 'Python')
