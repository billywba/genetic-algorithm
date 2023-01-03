import random

class Chromosome:
    def __init__(self, student_units, tutors, units):
        self.AMOUNT_OF_DAYS = 5
        self.EXAMS_PER_DAY = 2

        self.schedule = []
        for i in range (0, self.AMOUNT_OF_DAYS * self.EXAMS_PER_DAY):
            self.schedule.append([random.choice(student_units), random.choice(tutors), random.choice(units)])
