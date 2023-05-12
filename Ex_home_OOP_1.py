students_list = []
lecturer_list = []
course_list = []


class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_value = []
        students_list.append(self)

    def add_courses(self, course):
        self.finished_courses.append(course)

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_average_student_rating(self, students_grades):
        for item in students_grades.values():
            sum_all_val = sum(item) / len(item)
            self.average_value.append(sum_all_val)

    def __str__(self):
        return f'\nИмя студента: {self.name}\nФамилия студента: {self.surname}\nСредняя оценка за домашние задания: ' \
               f'{sum(self.average_value) / len(self.average_value)}\nКурсы в процессе изучения: ' \
               f'{", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'

    def __lt__(self, other):
        return self.average_value < other.average_value


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average = []
        lecturer_list.append(self)

    def get_average_lecturer_rating(self, lecturers_grades):
        total = 0
        for item in lecturers_grades.values():
            sum_v = total + (sum(item) / len(item))
            self.average.append(sum_v)

    def __str__(self):
        return f'\nИмя лектора: {self.name}\nФамилия лектора: {self.surname}\n' \
               f'Средняя оценка за лекции: {sum(self.average) / len(self.average)}'

    def __lt__(self, other):
        return self.average < other.average


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'\nИмя эксперта: {self.name}\nФамилия эксперта: {self.surname}'


print('\nЗадание № 1\n')

print(Lecturer.mro(), '\n')
print(Reviewer.mro(), '\n')

print('Задание № 2\n')

some_Lecturer = Lecturer('Some', 'Buddy')
some_Lecturer.courses_attached += ['Python']
some_Lecturer.courses_attached += ['Git']

some_student = Student('Roy', 'Eman', 'male')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Git']
some_student.finished_courses += ['Введение в программирование']

some_student.rate_lecture(some_Lecturer, 'Python', 10)
some_student.rate_lecture(some_Lecturer, 'Python', 9)
some_student.rate_lecture(some_Lecturer, 'Python', 8)
some_student.rate_lecture(some_Lecturer, 'Python', 10)
some_student.rate_lecture(some_Lecturer, 'Git', 9)

some_Reviewer = Reviewer('Some', 'Buddy')
some_Reviewer.courses_attached += ['Python']
some_Reviewer.courses_attached += ['Git']

some_Reviewer.rate_hw(some_student, 'Python', 10)
some_Reviewer.rate_hw(some_student, 'Python', 9)
some_Reviewer.rate_hw(some_student, 'Python', 8)
some_Reviewer.rate_hw(some_student, 'Python', 7)
some_Reviewer.rate_hw(some_student, 'Git', 7)

some_student.get_average_student_rating(some_student.grades)
some_Lecturer.get_average_lecturer_rating(some_Lecturer.grades)

print('Оценки студента за ДЗ, от эксперта', some_student.grades)
print('Оценки лектора за лекцию, от студента', some_Lecturer.grades)
print('\nЗадание № 3.1')
print(some_Reviewer)
print(some_Lecturer)
print(some_student)
print('\nЗадание № 3.2\n')
print('Сравнение средних оценок студентов и лекторов:\n')
print(f'Ср. балл у студента меньше, чем у лектора: {some_student.average_value < some_Lecturer.average}')
print(f'Ср. балл у студента больше, чем у лектора: {some_student.average_value > some_Lecturer.average}')

print('\nЗадание № 4\n')

first_Lecturer = Lecturer('Zed', 'A. Shaw')
first_Lecturer.courses_attached += ['Python']
first_Lecturer.courses_attached += ['Git']

second_Lecturer = Lecturer('Mark', 'Lutz')
second_Lecturer.courses_attached += ['Python']
second_Lecturer.courses_attached += ['Git']

first_student = Student('Петя', 'Васечкин', 'male')
first_student.courses_in_progress += ['Python']
first_student.courses_in_progress += ['Git']
first_student.finished_courses += ['Английский для программистов']
first_student.finished_courses += ['Введение в программирование']

second_student = Student('Вася', 'Петров', 'male')
second_student.courses_in_progress += ['Python']
second_student.courses_in_progress += ['Git']
second_student.finished_courses += ['Английский для программистов']
second_student.finished_courses += ['Введение в программирование']

first_Reviewer = Reviewer('John', 'Mueller')
first_Reviewer.courses_attached += ['Python']
first_Reviewer.courses_attached += ['Git']

second_Reviewer = Reviewer('Tony', 'Gaddis')
second_Reviewer.courses_attached += ['Python']
second_Reviewer.courses_attached += ['Git']

first_student.rate_lecture(first_Lecturer, 'Python', 10)
first_student.rate_lecture(first_Lecturer, 'Git', 9)
first_student.rate_lecture(second_Lecturer, 'Python', 8)
first_student.rate_lecture(second_Lecturer, 'Git', 10)

second_student.rate_lecture(first_Lecturer, 'Python', 10)
second_student.rate_lecture(first_Lecturer, 'Git', 9)
second_student.rate_lecture(second_Lecturer, 'Python', 8)
second_student.rate_lecture(second_Lecturer, 'Git', 9)

first_Reviewer.rate_hw(first_student, 'Git', 10)
first_Reviewer.rate_hw(first_student, 'Python', 9)
first_Reviewer.rate_hw(second_student, 'Git', 8)
first_Reviewer.rate_hw(second_student, 'Python', 7)

second_Reviewer.rate_hw(first_student, 'Python', 10)
second_Reviewer.rate_hw(first_student, 'Git', 6)
second_Reviewer.rate_hw(second_student, 'Python', 8)
second_Reviewer.rate_hw(second_student, 'Git', 5)

# передача словаря с оценками в метод get_average_student_rating класса Student
first_student.get_average_student_rating(first_student.grades)
second_student.get_average_student_rating(second_student.grades)
# передача словаря с оценками в метод get_average_lecturer_rating класса Lecturer
first_Lecturer.get_average_lecturer_rating(first_Lecturer.grades)
second_Lecturer.get_average_lecturer_rating(second_Lecturer.grades)

print('Оценки 1-го лектора за лекции: ', first_Lecturer.grades)
print('Оценки 2-го лектора за лекции: ', second_Lecturer.grades)
print('Оценки 1-го студента за ДЗ: ', first_student.grades)
print('Оценки 2-го студента за ДЗ: ', second_student.grades)
print(first_Reviewer)  # Получение имени и фамилии эксперта
print(second_Reviewer)
print(first_Lecturer)  # Получение имени, фамилии, средней оценки лектора
print(second_Lecturer)
print(first_student)  # Получение имени, фамилии, средней оценки и курсов студента
print(second_student)
# сравнение оценок лекторов и студентов
print('\nСравнение средних оценок студентов и лекторов:\n')
print(f'Ср. балл у Пети Васечкина меньше, чем у Васи Петрова: \
      {first_student.average_value < second_student.average_value}')
print(f'Ср. балл у Зеда А.Шоу больше, чем у Марка Лутца: {first_Lecturer.average > second_Lecturer.average}')
print('\nСредние баллы по группам:\n')


# Задание №4.1
def average_grade_students(students_list, course):
    course_list = ['Python', 'Git']
    total = 0
    count = 0
    if course in course_list:
        for student in students_list:
            for grade in student.grades[course]:
                total += grade
                count += 1
        return f'Средний балл студентов по курсу {course}: {round(total / count, 2)}.'
    return 'Такого курса нет.'


print(average_grade_students(students_list, 'Python'))
print(average_grade_students(students_list, 'Git'))
print(average_grade_students(students_list, 'Java'))


# Задание №4.2
def average_grade_lecturer(lecturer_list, course):
    course_list = ['Python', 'Git']
    total = 0
    count = 0
    if course in course_list:
        for lecturer in lecturer_list:
            for grade in lecturer.grades[course]:
                total += grade
                count += 1
        return f'Средний балл лекторов по курсу {course}: {round(total / count, 2)}.'
    return 'Такого курса нет.'


print()
print(average_grade_lecturer(lecturer_list, 'Python'))
print(average_grade_lecturer(lecturer_list, 'Git'))
print(average_grade_lecturer(lecturer_list, 'Java'))
