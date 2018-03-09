from student.student_utilities.grade_map import GradeMap


class Student:

    def __init__(self, age, name, korean, mathematics, english):
        self._age = age
        self._grade = GradeMap.instance().get_grade(age)
        self._name = name
        self._korean = korean
        self._mathematics = mathematics
        self._english = english


    @property
    def age(self):
        return self._age


    @property
    def grade(self):
        return self._grade


    @property
    def name(self):
        return self._name


    @property
    def korean(self):
        return self._korean


    @property
    def mathematics(self):
        return self._mathematics


    @property
    def english(self):
        return self._english


    @age.setter
    def age(self, value):
        self._age = value


    @grade.setter
    def grade(self, value):
        self._grade = GradeMap.instance().get_grade(value)


    @name.setter
    def name(self, value):
        self._name = value


    @korean.setter
    def korean(self, value):
        self._korean = value


    @mathematics.setter
    def mathematics(self, value):
        self._mathematics = value


    @english.setter
    def english(self, value):
        self._english = value