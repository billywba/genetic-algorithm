import random

class Chromosome:
    def __init__(self, student_units, tutors, units):
        self.AMOUNT_OF_DAYS = 5
        self.EXAMS_PER_DAY = 2
        self.rooms = ['P4' + str(i) for i in range(11, 21)]

        self.schedule = []
        for i in range (0, self.AMOUNT_OF_DAYS * self.EXAMS_PER_DAY):
            self.schedule.append([random.choice(self.rooms), random.choice(student_units), random.choice(tutors), random.choice(units)])

    def print_schedule(self):
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

        for i in range(0, len(days)):
            print(days[i])

            print(self.schedule[i * 2])
            print(self.schedule[i * 2 + 1])
