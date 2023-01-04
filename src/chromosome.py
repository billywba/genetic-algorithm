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
            morning_unit = self.schedule[i * 2]
            evening_unit = self.schedule[i * 2 + 1]
            
            print("| {:<61} |".format(days[i]))
            print("| Room | Morning Units | Tutors | Room | Evening Units | Tutors |")
            print("| {:<4} | {:<13} | {:<6} | {:<4} | {:<13} | {:<6} |\n".format(morning_unit[0], morning_unit[1], morning_unit[2], evening_unit[0], evening_unit[1], evening_unit[2]))
