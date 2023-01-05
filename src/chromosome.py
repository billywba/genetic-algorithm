import random

class Student:
    def __init__(self, name, units):
        self.name = name
        self.units = [units]

    def get_total_enrolled_units(self):
        return len(self.units)


class Chromosome:
    def __init__(self, student_units, tutors, units):
        self.AMOUNT_OF_DAYS = 5
        self.EXAMS_PER_DAY = 2

        self.students = [Student(info[1], info[2]) for info in student_units]

        self.units = units
        self.rooms = ['P4' + str(i) for i in range(11, 21)]

        self.schedule = []
        for i in range (0, self.AMOUNT_OF_DAYS * self.EXAMS_PER_DAY):
            self.schedule.append([random.choice(self.rooms), random.choice(units), random.choice(tutors), random.choice(units)])

    def evaluate_fitness(self):
        HARD_CONSTRAINT_SATISFACTION = 10
        SOFT_CONSTRAINT_SATISFACTION = 5

        fitness = 0

        ### HARD CONSTRAINTS ###

        # An exam will be scheduled for each unit. Unit name and code are presented in units.csv file.
        violation = False
        for unit in self.units:

            scheduled_unit_exams = []
            for exam in self.schedule:
                scheduled_unit_exams.append(exam[1])

            if unit not in scheduled_unit_exams:
                violation = True

        if not violation:
            fitness += HARD_CONSTRAINT_SATISFACTION

        # A student is enrolled at least one unit, but can be enrolled upto four units.
        if all(1 <= student.get_total_enrolled_units() <= 4 for student in self.students):
            fitness += HARD_CONSTRAINT_SATISFACTION

        # A student cannot appear in more than one exam at a time.
        fitness += HARD_CONSTRAINT_SATISFACTION

        # Exam won’t be held on the weekends i.e., on Saturday and Sunday.
        fitness += HARD_CONSTRAINT_SATISFACTION

        # Each exam must be invigilated by a tutor. You can get tutor information using tutor.csv file. You should display tutor
        # name in the output.
        if not any(exam[2] == "" for exam in self.schedule):
            fitness += HARD_CONSTRAINT_SATISFACTION

        # A tutor invigilates one exam at a time.
        if all(len(exam[2]) == 1 for exam in self.schedule):
            fitness += HARD_CONSTRAINT_SATISFACTION


        # Each exam must be conducted between 10:00 am to 4:00 pm.
        fitness += HARD_CONSTRAINT_SATISFACTION

        ### SOFT CONSTRAINTS ###

        # Student should not sit in more than one exam consecutively in a day. In other word, if a student sits in exam on
        # Monday in the morning slot, then don’t schedule another exam for the same student in the afternoon slot.

        # Try to assign equal number of invigilation duties to each tutor.

        # Count how many exams each tutor is invigilating
        tutor_counts = { }
        for exam in self.schedule:
            tutor = exam[2]
            if tutor not in tutor_counts:
                tutor_counts[tutor] = 1
            else:
                tutor_counts[tutor] += 1

        if max(tutor_counts.values()) - min(tutor_counts.values()) < 1:
            fitness += HARD_CONSTRAINT_SATISFACTION

        return fitness

    def print_schedule(self):
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

        for i in range(0, len(days)):
            morning_unit = self.schedule[i * 2]
            evening_unit = self.schedule[i * 2 + 1]
            
            print("| {:<61} |".format(days[i]))
            print("| Room | Morning Units | Tutors | Room | Evening Units | Tutors |")
            print("| {:<4} | {:<13} | {:<6} | {:<4} | {:<13} | {:<6} |\n".format(morning_unit[0], morning_unit[1], morning_unit[2], evening_unit[0], evening_unit[1], evening_unit[2]))
