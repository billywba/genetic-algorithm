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
        self.tutors = tutors
        self.rooms = ['P4' + str(i) for i in range(11, 21)]
        self.days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        self.exam_times = [day + '_' + time_period for day in self.days for time_period in ['AM', 'PM']]

        self.schedule = []
        for i in range (0, len(self.units)):
            self.schedule.append([random.choice(self.rooms), random.choice(self.units), 
                                    random.choice(self.tutors), random.choice(self.exam_times)])

    def evaluate_fitness(self):
        self.fitness = 0

        hard_constraint_functions = [
                                        self.schedule_has_exam_for_each_unit_hard_constraint,
                                        self.student_enrolled_in_correct_units_hard_constraint,
                                        self.student_has_one_exam_at_a_time_hard_constaint,
                                        self.exam_not_on_weekend_hard_constraint,
                                        self.exam_has_tutor_invigilating_hard_constraint,
                                        self.tutor_invigilates_one_exam_at_a_time_hard_constraint,
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
        # Get units which have an exam scheduled
        scheduled_unit_exams = [exam[1] for exam in self.schedule]
        
        # If unit not present in generated exam schedule, increase violations
        violations = 0
        for unit in self.units:
            if unit not in scheduled_unit_exams:
                violations += 1

        return violations

    # A student is enrolled at least one unit, but can be enrolled upto four units.
    def student_enrolled_in_correct_units_hard_constraint(self):
        return all(1 <= student.get_total_enrolled_units() <= 4 for student in self.students)

    # A student cannot appear in more than one exam at a time.
    def student_has_one_exam_at_a_time_hard_constaint(self):
        return 0

    # Exam won’t be held on the weekends i.e., on Saturday and Sunday.
    def exam_not_on_weekend_hard_constraint(self):
        return 0

    # Each exam must be invigilated by a tutor. You can get tutor information using tutor.csv file. You should display tutor
    # name in the output.
    def exam_has_tutor_invigilating_hard_constraint(self):
        violations = 0
        for exam in self.schedule:
            if exam[2] == "":
                violations += 1

        return violations

    # A tutor invigilates one exam at a time.
    def tutor_invigilates_one_exam_at_a_time_hard_constraint(self):
        violations = 0

        # Get current exams at each time period
        for exam_time in self.exam_times:

            # Get list of current exams and the tutors
            current_exams = [exam for exam in self.schedule if exam[3] == exam_time]
            current_tutors = [exam[2] for exam in current_exams]
            
            # Check if tutor is invigilating more than one exam at the current time period
            for tutor in current_tutors:
                if current_tutors.count(tutor) > 1:
                    violations += 1
                    continue

        return violations

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

    def mutate(self, mutation_probability):
        if random.uniform(0, 1) < mutation_probability:
            # Get a random exam to be changed
            mutated_exam_index = random.randint(0, len(self.schedule) - 1)
            mutate_choice = random.randint(0, 2)

            if mutate_choice == 0:
                # Change room
                self.schedule[mutated_exam_index][0] = random.choice(self.rooms)
            elif mutate_choice == 1:
                # Change unit
                self.schedule[mutated_exam_index][1] = random.choice(self.units)
            else:
                # Change tutor
                self.schedule[mutated_exam_index][2] = random.choice(self.tutors)

    def print_schedule(self):
        for exam_time in self.exam_times:
            print(exam_time)
            print("| Room | Unit   | Tutors  |")

            for exam in self.schedule:
                if exam[3] == exam_time:
                    print("| {:<4} | {:<6} | {:<6} |".format(exam[0], exam[1], exam[2]))

            print("\n")