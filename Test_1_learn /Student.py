class Student:

    def __init__(self, name, major, gpa, is_on_probation, grade):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
        self.grade = grade

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

    def is_on_probation(self):
        if self.gpa < 3.0:
            return True
        else:
            return False
