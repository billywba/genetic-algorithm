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

        self.HARD_CONSTRAINT_SATISFACTION = 10
        self.SOFT_CONSTRAINT_SATISFACTION = 5
        self.fitness = 0

        self.students = [Student(info[1], info[2]) for info in student_units]

        self.units = units
        self.rooms = ['P4' + str(i) for i in range(11, 21)]

        self.schedule = []
        for i in range (0, self.AMOUNT_OF_DAYS * self.EXAMS_PER_DAY):
            self.schedule.append([random.choice(self.rooms), random.choice(units), random.choice(tutors)])

    def evaluate_fitness(self):
        self.fitness = 0

        hard_constraint_functions = [
                                        self.schedule_has_exam_for_each_unit_hard_constraint,
                                        self.student_enrolled_in_correct_units_hard_constraint,
                                        self.student_has_one_exam_at_a_time_hard_constaint,
                                        self.exam_not_on_weekend_hard_constraint,
                                        self.exam_has_tutor_invigilating_hard_constraint,
                                        self.exam_has_one_tutor_invigilating_hard_constraint,
                                        self.exam_is_conducted_between_start_and_end_time
                                    ]

        soft_constraint_functions = [
                                        self.student_does_not_sit_more_than_one_exam_per_day_soft_constraint,
                                        self.schedule_has_equal_tutor_invigilation_soft_constraint
                                    ]

        for hard_constraint in hard_constraint_functions:
            self.fitness += self.HARD_CONSTRAINT_SATISFACTION if hard_constraint() else 0

        for soft_constraint in soft_constraint_functions:
            self.fitness += self.SOFT_CONSTRAINT_SATISFACTION if soft_constraint() else 0

        return self.fitness


    ### HARD CONSTRAINTS ###

    # An exam will be scheduled for each unit. Unit name and code are presented in units.csv file.
    def schedule_has_exam_for_each_unit_hard_constraint(self):
        violation = False
        for unit in self.units:

            scheduled_unit_exams = []
            for exam in self.schedule:
                scheduled_unit_exams.append(exam[1])

            if unit not in scheduled_unit_exams:
                violation = True

        return not violation

    # A student is enrolled at least one unit, but can be enrolled upto four units.
    def student_enrolled_in_correct_units_hard_constraint(self):
        return all(1 <= student.get_total_enrolled_units() <= 4 for student in self.students)

    # A student cannot appear in more than one exam at a time.
    def student_has_one_exam_at_a_time_hard_constaint(self):
        return True

    # Exam won’t be held on the weekends i.e., on Saturday and Sunday.
    def exam_not_on_weekend_hard_constraint(self):
        return True

    # Each exam must be invigilated by a tutor. You can get tutor information using tutor.csv file. You should display tutor
    # name in the output.
    def exam_has_tutor_invigilating_hard_constraint(self):
        return not any(exam[2] == "" for exam in self.schedule)

    # A tutor invigilates one exam at a time.
    def exam_has_one_tutor_invigilating_hard_constraint(self):
        return all(not isinstance(exam[2], list) for exam in self.schedule)

    # Each exam must be conducted between 10:00 am to 4:00 pm.
    def exam_is_conducted_between_start_and_end_time(self):
        return True

    ### SOFT CONSTRAINTS ###

    # Student should not sit in more than one exam consecutively in a day. In other word, if a student sits in exam on
    # Monday in the morning slot, then don’t schedule another exam for the same student in the afternoon slot.
    def student_does_not_sit_more_than_one_exam_per_day_soft_constraint(self):
        violation = False

        for i in range(0, int(len(self.schedule) / 2), 2):
            if self.schedule[i][1] == self.schedule[i + 1][1]:
                violation = True

        return not violation

    # Try to assign equal number of invigilation duties to each tutor.
    def schedule_has_equal_tutor_invigilation_soft_constraint(self):
        # Count how many exams each tutor is invigilating
        tutor_counts = { }
        for exam in self.schedule:
            tutor = exam[2]
            if tutor not in tutor_counts:
                tutor_counts[tutor] = 1
            else:
                tutor_counts[tutor] += 1

        return max(tutor_counts.values()) - min(tutor_counts.values()) < 1


    def print_schedule(self):
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

        for i in range(0, len(days)):
            morning_unit = self.schedule[i * 2]
            evening_unit = self.schedule[i * 2 + 1]
            
            print("| {:<62} |".format(days[i]))
            print("| Room | Morning Units | Tutors  | Room | Evening Units | Tutors |")
            print("| {:<4} | {:<13} | {:<6} | {:<4} | {:<13} | {:<6} |\n".format(morning_unit[0], morning_unit[1], morning_unit[2], evening_unit[0], evening_unit[1], evening_unit[2]))
